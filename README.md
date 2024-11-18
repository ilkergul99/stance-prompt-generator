# Stance Detection Prompt Generator

This project is a utility for generating zero-shot and few-shot prompts for stance detection tasks. It processes datasets containing tweets and their corresponding targets, dynamically applies prompt templates for various models, and outputs the results as JSON files.

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Folder Structure](#folder-structure)
4. [Dependencies](#dependencies)
5. [Usage](#usage)
    - [Zero-Shot Prompt Generation](#zero-shot-prompt-generation)
    - [Few-Shot Prompt Generation](#few-shot-prompt-generation)
6. [Generated Output](#generated-output)
7. [Adding Support for New Models](#adding-support-for-new-models)
8. [Citation](#citation)

---

## Overview

The `stance_detection` package provides tools for generating zero-shot and few-shot prompts from stance detection datasets. The prompts are tailored for various datasets (e.g., SemEval 2016, PStance, Twitter Stance KEMLM) and models (e.g., Qwen, LLaMA2, Mistral). The final output is a JSON file that includes metadata and dynamically generated prompts.

---

## Features

- **Dataset Compatibility**: Works with datasets like SemEval 2016, PStance, and Twitter Stance KEMLM.
- **Model Agnostic**: Supports various models including Qwen, Mistral, and LLaMA2.
- **Dynamic Prompt Templates**: Leverages dynamically selected template functions for generating model-specific prompts.
- **Flexible Input Handling**: Processes datasets with varying column names (`Tweet`, `tweet`, `Target`, `target`).
- **Few-Shot Examples**: Supports the inclusion of few-shot examples selected randomly from the train/validation files.
- **Customizable Output**: Generates JSON files with filenames based on dataset, model, and candidate names.

---

## Folder Structure

```plaintext
.
├── stance_detection/
│   ├── generate_zero_shot_prompts.py
│   ├── generate_few_shot_prompts.py
│   ├── prompts.py
│   └── __init__.py
├── data/
│   ├── semeval2016/
│   │   ├── train.csv
│   │   ├── test.csv
│   ├── PStance/
│   │   ├── raw_test_bernie.csv
│   │   ├── raw_test_biden.csv
│   │   ├── raw_test_trump.csv
│   │   ├── raw_train_bernie.csv
│   │   ├── raw_train_biden.csv
│   │   ├── raw_train_trump.csv
│   │   ├── raw_val_bernie.csv
│   │   ├── raw_val_biden.csv
│   │   ├── raw_val_trump.csv
│   └── twitter_stance_kemlm/
│       ├── biden_stance_test_public.csv
│       ├── biden_stance_train_public.csv
│       ├── trump_stance_test_public.csv
│       ├── trump_stance_train_public.csv
├── output/
│   └── (Generated JSON files will be saved here)
└── README.md
```

---

## Dependencies

Make sure the following Python packages are installed:

- Python 3.8+
- `csv`
- `json`

---

Here’s the updated **Usage** section with clear instructions tailored for both the zero-shot and few-shot scripts. Additionally, I’ve included example bash scripts for running each script.

---

## Usage

### Zero-Shot Prompt Generation

Zero-shot prompts are generated without using few-shot examples. The input is a dataset file containing tweets and targets, and the output is a JSON file with the generated prompts.

#### Input Files

The input files must contain at least two columns:
- `Tweet` or `tweet`: The text of the tweet.
- `Target` or `target`: The entity being analyzed.

#### Running the Zero-Shot Script

1. **Navigate to the Project Directory**:
   ```bash
   cd /path/to/project
   ```

2. **Run the `generate_zero_shot_prompts` Script**:
   ```bash
   python stance_detection/generate_zero_shot_prompts.py --input_csv data/PStance/raw_test_bernie.csv \
                                        --output_dir output \
                                        --dataset_name PStance \
                                        --model_name qwen2 \
                                        --candidate_name bernie
   ```

3. **Parameters**:
   - `--input_csv`: Path to the input dataset file.
   - `--output_dir`: Directory where the generated JSON file will be saved.
   - `--dataset_name`: The name of the dataset (e.g., `PStance`, `semeval2016`).
   - `--model_name`: The name of the model (e.g., `qwen2`, `llama2`).
   - `--candidate_name`: Candidate name (optional; required for `PStance` and `twitter_stance_kemlm`).

#### Example Bash Script: Zero-Shot Prompts
Create a script file, e.g., `run_zero_shot.sh`:
```bash
#!/bin/bash

python stance_detection/generate_zero_shot_prompts.py --input_csv data/PStance/raw_test_bernie.csv \
                                     --output_dir output \
                                     --dataset_name PStance \
                                     --model_name qwen2 \
                                     --candidate_name bernie

python stance_detection/generate_zero_shot_prompts.py --input_csv data/semeval2016/test.csv \
                                     --output_dir output \
                                     --dataset_name semeval2016 \
                                     --model_name llama2
```

Run the script:
```bash
bash run_zero_shot.sh
```

---

### Few-Shot Prompt Generation

Few-shot prompts include examples randomly selected from the train/validation files. The examples are appended to the prompt for better contextual understanding.

#### Input Files for Few-Shot

- **PStance**: Validation files (e.g., `raw_val_bernie.csv`) are used for selecting few-shot examples.
- **twitter_stance_kemlm**: Train files (e.g., `biden_stance_train_public.csv`) are used for selecting few-shot examples.
- **semeval2016**: Train files (e.g., `train.csv`) are used for selecting few-shot examples.

#### Running the Few-Shot Script

1. **Navigate to the Project Directory**:
   ```bash
   cd /path/to/project
   ```

2. **Run the Few-Shot Script**:
   - For **PStance**:
     ```bash
     python stance_detection/generate_few_shot_prompts.py --dataset_dir data/PStance \
                                         --output_dir output \
                                         --dataset_name PStance \
                                         --model_name qwen2 \
                                         --candidate_name bernie \
                                         --examples_count 3
     ```
   - For **Twitter Stance KEMLM**:
     ```bash
     python stance_detection/generate_few_shot_prompts.py --dataset_dir data/twitter_stance_kemlm \
                                         --output_dir output \
                                         --dataset_name twitter_stance_kemlm \
                                         --model_name llama2 \
                                         --candidate_name biden \
                                         --examples_count 3
     ```
   - For **SemEval 2016**:
     ```bash
     python stance_detection/generate_few_shot_prompts.py --dataset_dir data/semeval2016 \
                                         --output_dir output \
                                         --dataset_name semeval2016 \
                                         --model_name qwen2 \
                                         --examples_count 3
     ```

---

### Output Files

The generated prompts will be saved in the `output/` directory with filenames that follow this format:
- **Zero-Shot**:
  - `PStance_qwen2_bernie_prompts.json`
  - `semeval2016_llama2_prompts.json`
- **Few-Shot**:
  - `PStance_qwen2_bernie_few_shot_prompts.json`
  - `twitter_stance_kemlm_llama2_biden_few_shot_prompts.json`
  - `semeval2016_qwen2_few_shot_prompts.json`

---

This updated **Usage** section and bash scripts make it easy to generate both zero-shot and few-shot prompts for your datasets and models. Let me know if you need further refinements! 😊

## Generated Output

### Zero-Shot Output
Example file name:
```
output/PStance_qwen2_prompts.json
```

### Few-Shot Output
File names depend on the dataset and candidate:
- **PStance (Bernie)**:
  ```
  output/PStance_qwen2_bernie_few_shot_prompts.json
  ```
- **Twitter Stance KEMLM (Biden)**:
  ```
  output/twitter_stance_kemlm_llama2_biden_few_shot_prompts.json
  ```
- **SemEval 2016**:
  ```
  output/semeval2016_qwen2_few_shot_prompts.json
  ```

### Example JSON Content
```json
[
    {
        "dataset": "PStance",
        "model": "qwen2",
        "tweet": "This is an example tweet about Bernie Sanders.",
        "target": "Bernie Sanders",
        "prompt": "Generated prompt here..."
    }
]
```

---

## Adding Support for New Models

1. **Create a Template**:
   Add a new prompt template function in `stance_detection/prompts.py`.

   Example:
   ```python
   def semeval2016_newmodel_few_shot_template(tweet: str, target: str, examples: list) -> str:
       return f"<new_template> Tweet: {tweet}, Target: {target}, Examples: {examples}"
   ```

2. **Import the Template**:
   Ensure the template is imported in your main script.

3. **Run the Script**:
   Use the new model name when invoking the script.

---

Here’s the updated **Citation** section with website links for EPFL and the LSIR Lab:

---

## Citation

This repository is part of the research work conducted at the **LSIR Lab** (Distributed Information Systems Laboratory), **École Polytechnique Fédérale de Lausanne (EPFL)**. The LSIR Lab focuses on developing methods and systems that turn unstructured, heterogeneous and untrusted data into meaningful, reliable and understandeable information. More information about EPFL and LSIR Lab can be found at:

- [EPFL Official Website](https://www.epfl.ch)
- [LSIR Lab Website](https://www.epfl.ch/labs/lsir/)

This repository is designed to support experiments and evaluations in stance detection on social media using fine-tuned large language models. The tools provided enable generating prompts for both **zero-shot** and **few-shot** settings, facilitating testing, benchmarking, and comparison of model performance. This repository also serves as a foundation for fine-tuning tasks and related research in stance detection.

If you find this work useful in your research or applications, please cite the following paper:

```
@misc{gül2024stancedetectionsocialmedia,
      title={Stance Detection on Social Media with Fine-Tuned Large Language Models}, 
      author={İlker Gül and Rémi Lebret and Karl Aberer},
      year={2024},
      eprint={2404.12171},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2404.12171}, 
}
```

---
