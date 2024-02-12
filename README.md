UNLP 2024 Shared Task on Fine-Tuning Large Language Models (LLMs) for Ukrainian
===============================================================================

The Third Ukrainian NLP workshop ([UNLP 2024](https://unlp.org.ua/))
organizes the first Shared Task on Fine-Tuning Large Language Models
(LLMs) for Ukrainian. This Shared Task aims to challenge and assess
LLMs' capabilities to understand and generate Ukrainian, paving the way
for LLM development in Slavic languages.

Registration form: https://forms.gle/MiC7pWsWbwBdSmoX9

Please register **by February 22, 2024** and join the discussions in Discord
via https://discord.gg/kCc6xgWbCJ.

Updates
-------

**2024-02-12**:

* Update important dates.
* Release training data for [exam questions](./data/zno.train.jsonl).
* Release sample [open questions](./data/open-questions.train.jsonl).

Task description
----------------

In this shared task, your goal is to instruction-tune a large language
model that can answer questions and perform tasks in Ukrainian. The
model should possess knowledge of Ukrainian history, language, and
literature, as well as common knowledge, and should be capable of
generating fluent and factually accurate responses.

Instruction tuning may be complemented by various prompting strategies,
like few-shot learning or chain-of-thought reasoning. You can also use
retrieval augmented generation from open data sources.

We encourage you to use any open external data of your choice
(Wikipedia, textbooks, grammar books, etc.) except for the Ukrainian
External Independent Evaluation.

For an easy start with the competition, consider this guide on
fine-tuning with Llama 2 using QLoRA:

* https://www.kaggle.com/code/philculliton/fine-tuning-with-llama-2-qlora


Datasets
--------

We provide two datasets that you can use for tuning your models.
We will evaluate your models on a hidden set of similar data.

## 1. Exam questions

Data location: [`./data/zno.train.jsonl`](./data/zno.train.jsonl) or
https://huggingface.co/datasets/osyvokon/zno

This dataset contains machine-readable questions and answers from Ukrainian
External independent testing (called _ЗНО_/_ZNO_ in Ukrainian).

Question subjects are:

- History of Ukraine
- Ukrainian language and literature

A training set contains 3063 question/answers. We will release a test set soon.

Every line in a .jsonl file contains a structure like this:

```js
{
  "question": "На другий склад падає наголос у слові",
  "answers": [
    { "marker": "А", "text": "начинка" },
    { "marker": "Б", "text": "випадок" },
    { "marker": "В", "text": "дрова" },
    { "marker": "Г", "text": "загадка" },
    { "marker": "Д", "text": "русло" }
  ],
  "correct_answers": ["Д"],
  "subject": "ukrainian-language-and-literature"
}
```

Currently, all questions have exactly one correct answer (`correct_answers[0]`).


### 2. Open questions

Data location: [`./data/open-questions.train.jsonl`](./data/open-questions.train.jsonl).

This set of instruction prompts ask to perform a text generation tasks,
like text summarization, short story and poem generation, adding
explanations to sample text, question answering, and so on.
questions will contain references to the history, culture, literature,
music, and geography of Ukraine, as well as cover multiple genres of
writing.

Those questions don't have a single correct answer. They will be
used for manual side-by-side comparison of model outputs.

A sample record from a provided JSON lines file:

```json
{
  "instruction": "Розкажи сюжет казки \"Котик і Півник\".",
  "input": "",
  "output": ""
}
```

`input` and `output` are currently empty and are provided for compatibility
with the Alpaca dataset format.


Limitations
-----------

To ensure fair competition with reproducible results, please adhere to
the following limitations:

1.  Only LLMs with open weights such as Llama-2, Mistral, Phi-2, etc.
    are allowed for the shared task.

2.  The model should be able to run on GPU with 16GB VRAM and CUDA
    compute capacity 8.6. Some examples of suitable GPUs include NVIDIA
    GeForce RTX 3080/4090, RTX A4000, and A2.

    - You are not limited in the type and amount of compute that you use for
      training.

    - The model weights and activations should fit and stay in GPU memory
      entirely. CPU memory and disk offloading is not allowed.

    - You can use external storage for retrieval-augmented generation and
      other non-parametric methods.

3.  The weights of the final model should be published on [the Hugging
    Face Hub](https://huggingface.co/) or a similar open platform.

4.  If you're going to train on Ukrainian External Independent Evaluation ("ЗНО")
    data, use [the provided data](./data/zno.train.jsonl) to avoid
    test set contamination.


Evaluation
----------

Model evaluation will be twofold:

-   Automated evaluation — the **accuracy** of the model's answers to
    multiple-choice questions. The questions are based on the Ukrainian
    External Independent Evaluation tasks related to the topics of
    Ukrainian history, language, and literature.

    We provide a sample of data that you can use for training and
    validating your model: [./data/zno.train.jsonl](./data/zno.train.jsonl).

    The test data is to be released on February 16, 2024.

-   Human evaluation — **manual evaluation** of text generation tasks,
    like text summarization, short story and poem generation, adding
    explanations to sample text, question answering, free chat. Open
    questions will contain references to the history, culture, literature,
    music, and geography of Ukraine, as well as cover multiple genres of
    writing. The evaluation will be organized as a side-by-side comparison
    of random model outputs.

    Please find sample prompts in [./data/open-questions.train.jsonl](./data/open-questions.train.jsonl).

    We will release a set of test prompts on February 16, 2024.



Submission
----------

TBD

Baselines
---------

See [./examples/random_baseline.py](./examples/random_baseline.py) for
a very simple (and useless) baseline that always answers with the first
choice. This script contains code to load the dataset and to generate a
sample prompt. Use it to get the idea behind the data structure and
automated evaluation.

Publication
-----------

Participants in the shared task are invited to submit a paper to the
UNLP 2024 workshop. Please see the [UNLP website](https://unlp.org.ua/)
for details. Accepted papers will appear in the ACL anthology and will
be presented at a session of UNLP 2024 specially dedicated to the Shared
Task.

Submitting a paper is **not mandatory** for participating in the Shared
Task.

Important Dates
---------------

January 15, 2024 — Shared task announcement\
February 12, 2024 — Second call for participation; release of train data\
February 16, 2024 — Release of test data to registered participants\
February 24, 2024 — Registration deadline; release of open questions\
February 26, 2024 — Submission of system responses\
March 4, 2024 — Results of the Shared Task announced\
March 6, 2024 — Shared Task paper due\
March 27, 2024 — Notification of acceptance\
April 5, 2024 — Camera-ready Shared Task papers due\
May 25, 2024 — Workshop date

Contacts
--------

Email: oleksiy.syvokon@gmail.com

Discord: https://discord.gg/kCc6xgWbCJ

References
----------

- [UNLP 2024 Call for Papers](https://unlp.org.ua/call-for-papers/)
