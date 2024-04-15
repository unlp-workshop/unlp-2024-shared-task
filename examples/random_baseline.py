#!/usr/bin/env python3
"""This "model" always picks the first choice as an answer.

It's a simple but useless baseline.

Usage:
    ./random_baseline.py [dataset_path] [--verbose]

Options:
    dataset_path: Path to a json-lines file. If not provided, use the sample dataset.
    --verbose: If set, print the generated prompts.

"""

import json
import argparse
import textwrap
import os
from dataclasses import dataclass


@dataclass
class Choice:
    marker: str
    text: str
    # group: str   # Unused for now


@dataclass
class Task:
    question: str
    choices: list[Choice]
    correct_answers: list[str]
    source: str

    @staticmethod
    def from_dict(data: dict) -> "Task":
        return Task(
            question=data["question"],
            choices=[Choice(**choice) for choice in data["answers"]],
            correct_answers=data["correct_answers"],
            source=data["subject"],
        )


def predict(dataset: list[Task], *, verbose=True) -> list[str]:
    """Make a prediction on a dataset."""

    answers = []
    for sample in dataset:
        # We don't really need a prompt to make a random prediction.
        # Nevertheless, we list the steps here to match the real
        # use-case closer.
        prompt = make_prompt(sample)
        completion = complete(prompt)
        answer = parse_completion(completion)
        answers.append(answer)

        if verbose:
            print(prompt)
            print(f"### Answer: {answer}")
            print()
            print("--------------")

    return answers


def make_prompt(task: Task) -> str:
    """Make an LLM prompt for the given task."""

    prompt_template = textwrap.dedent(
        """\
        {question}

        {choices}

        {extra_instructions}
    """
    )
    choices = format_choices(task.choices)
    extra_instructions = format_extra_instructions(task)
    prompt = prompt_template.format(
        question=task.question,
        choices=choices,
        extra_instructions=extra_instructions,
    )
    return prompt


def format_choices(choices: list[Choice]) -> str:
    result = ""
    for choice in choices:
        result += f"{choice.marker}. {choice.text}\n"
    return result


def format_extra_instructions(task: Task) -> str:
    if len(task.correct_answers) == 1:
        # Single-choice question is the only possible type right now
        if task.choices:
            # For example, " (А-Г)"
            range_hint = f" ({task.choices[0].marker}-{task.choices[-1].marker})"
        else:
            range_hint = ""
        instructions = f"Вкажіть першу літеру правильної відповіді{range_hint} або '-', якщо відповісти літерою неможливо."

    else:
        # Multiple-choice and open questions are not supported yet
        instructions = ""

    return instructions


def complete(prompt: str) -> str:
    """Make a completion on the given prompt."""

    # Normally, you'd generate it from a language model
    return "А"


def parse_completion(completion: str) -> str:
    """Parse a completion into an answer."""

    # Normally, you'd have a code that extracts answers
    # from whatever the model can produce.
    # In our case, the completion is fixed, so we can just
    # return it as-is.
    return completion


def compute_metric(dataset: list[Task], answers: list[str]) -> float:
    """Compute the metric on the given dataset and answers."""

    assert len(dataset) == len(answers)

    correct = 0
    for sample, answer in zip(dataset, answers):
        if answer in sample.correct_answers:
            correct += 1

    return correct / len(dataset)


def load_dataset(path: str) -> list[Task]:
    dataset = []
    with open(path) as f:
        for line in f:
            task = Task.from_dict(json.loads(line))
            dataset.append(task)
    return dataset


if __name__ == "__main__":
    data_dir = os.path.join(os.path.dirname(__file__), "../data")
    sample_path = os.path.join(data_dir, "llm-for-ua-sample.jsonl")

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "dataset",
        help="Path to the dataset (json-lines file).",
        nargs="?",
        default=sample_path,
    )
    parser.add_argument("--verbose", action="store_true", help="Print generated prompt")
    args = parser.parse_args()

    dataset = load_dataset(args.dataset)
    answers = predict(dataset, verbose=args.verbose)
    accuracy = compute_metric(dataset, answers)

    print(f"Accuracy: {accuracy:.0%}")
