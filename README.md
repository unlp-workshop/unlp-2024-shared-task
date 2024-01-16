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

Limitations
-----------

To ensure fair competition with reproducible results, please adhere to
the following limitations:

1.  Only LLMs with open weights such as Llama-2, Mistral, Phi-2, etc.
    are allowed for the shared task.
2.  The model should be able to run on GPU with 16GB VRAM and CUDA
    compute capacity 8.6. Some examples of suitable GPUs include NVIDIA
    GeForce RTX 3080/4090, RTX A4000, and A2. You are not limited in the
    type and amount of compute that you use for training.
3.  The weights of the final model should be published on [the Hugging
    Face Hub](https://huggingface.co/) or a similar open platform.
4.  The data from the Ukrainian External Independent Evaluation (EIE)
    cannot be used for instruction tuning.

Evaluation
----------

Model evaluation will be twofold:

-   Automated evaluation --- the **accuracy** of the model's answers to
    multiple-choice questions. The questions are based on the Ukrainian
    External Independent Evaluation tasks related to the topics of
    Ukrainian history, language, and literature. Please find sample
    questions in [llm-for-ua-sample.jsonl](data/llm-for-ua-sample.jsonl).

-   Human evaluation --- **manual ratings** of text generation tasks,
    like text summarization, short story and poem generation, adding
    explanations to sample text, free chat.

Submission
----------

TBD

Baselines
---------

See [./examples/random\_baseline.py](./examples/random_baseline.py) for
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

January 15, 2024 --- Shared task announcement\
February 15, 2024 --- Release of test data to registered participants\
February 22, 2024 --- Registration deadline\
February 23, 2024 --- Submission of system responses\
March 1, 2024 --- Shared Task paper due\
March 7, 2024 --- Results of the Shared Task announced\
March 29, 2024 --- Notification of acceptance\
TBD (mid-April) --- Camera-ready Shared Task papers due\
May 25, 2024 --- Workshop date

Contacts
--------

Email: oleksiy.syvokon@gmail.com

Discord: https://discord.gg/kCc6xgWbCJ

References
----------

- [UNLP 2024 Call for Papers](https://unlp.org.ua/call-for-papers/)
