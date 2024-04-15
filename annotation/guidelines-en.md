## Guidelines for the evaluation of LLM quality at the UNLP-2024 shared task

Annotator chat: https://t.me/+fzZDVJuKLnNiYTcy.

Organizers: @mariana_scorp (Mariana Romanyshyn), @Salad_g (Roman Kyslyi), @osyvokon (Oleksiy Syvokon).

Timeline: February 28 – March 3, 2024.

## Context

The [Ukrainian NLP 2024](https://unlp.org.ua/) workshop features the first [Shared Task](https://unlp.org.ua/shared-task/) on Fine-Tuning Large Language Models (LLMs) for Ukrainian.

Goals of the shared task:
* to encourage research aimed at enriching large language models with knowledge about Ukraine, the Ukrainian language, culture, history, etc.;
* to create a platform for a fair comparison of the quality of large language models for the Ukrainian language;
* to show an example of using open data for training and testing large language models for the Ukrainian language.

We prepared a test set with a hundred open questions for the participants of the shared task. In addition to questions about Ukraine, the Ukrainian language, culture, history, etc., the test set also included instructions to generate a certain type of text. Examples of questions in the test set:

    Розкажи сюжет казки "Котик і Півник".  
    Transl: Tell me the plot of the fairy tale "The Cat and the Rooster".
    
    Дніпро — це річка чи місто?
    Transl: Is Dnipro a river or a city?
    
    Ось текст:
    ```Сіється сніг. В дерев'яній клітці здоровенний тигр роззявив пащу, реве. Збоку стоять чотири мисливці, виструнчившись перед оком апарата, спираючись на рушниці. Один старий мисливець і три молодих. Всі в чуднім одязі — в шкіряних штанях, химерних, у шкіряних піджаках, підперезані набійнищями. Три в шапочках, один — без. І той "без" — Наталка! Так, Наталка! Стоїть, спершись на вінчестер, дивиться насмішкувато. Вуста міцно стулені, очі примружені, голова непокрита, і на неї падають сніжинки...```
    Скільки мисливців було в тексті?
    Transl: Here's a text: ```<excerpt from "Tiger Trappers" by Ivan Bahrianyi>``` How many hunters were there in the text?

We received six submissions with answers to the open questions from different LLMs, and now we need to determine which model works best with the Ukrainian language.

## The task

1. Go to https://huggingface.co/spaces/woters/unlp.
2. Click Start. At this point, you will see the question (above) and answers of two random models (right and left).
3. Choose which of the two models answered the question better.
   * Vote for Model 1 — the model on the left did better
   * Vote for Model 2 — the model on the right did better
   * It's a tie! - equally good or equally bad
4. The tool will automatically load the next question.

_Known issue:_ some questions contain text in a highlighted window, and it needs to be scrolled to the right. Unfortunately, there is no way to fix this inconvenience.

## How to evaluate

Below are the prioritized criteria for evaluation:
1. The answer must be in Ukrainian.  
   _The Ukrainian language wins over other languages._
2. The answer must answer the question / follow the instructions.  
   _A poorly written answer to a question wins over a well-written answer that doesn't address the question._
3. The answer must be factually correct. This includes questions about language, culture, history, music, literature, and geography.
4. The answer must be grammatically and stylistically correct.
5. The answer is subjectively more to your liking. Yes, this is also important.

💡 A longer answer is not always a better answer.

## Afterword

We are incredibly grateful for your time and for helping to develop tools for processing the Ukrainian language ❤️

Write your questions, comments, and wishes in the chat! 
