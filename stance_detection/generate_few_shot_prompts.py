import os
import csv
import json
import random
import argparse
from prompts import *  # Import all your prompt functions


def generate_few_shot_prompts(dataset_dir: str, output_dir: str, dataset_name: str, model_name: str, candidate_name: str = None, examples_count: int = 3):
    """
    Generates few-shot prompts using examples from train/validation files and questions from test files.
    Includes candidate name filtering for PStance and twitter_stance_kemlm datasets.

    Args:
        dataset_dir (str): Directory containing the dataset files.
        output_dir (str): Directory where the output JSON file will be saved.
        dataset_name (str): Name of the dataset to use (e.g., "PStance", "semeval2016", "twitter_stance_kemlm").
        model_name (str): Name of the model to use for generating prompts (e.g., "qwen2").
        candidate_name (str): Name of the candidate (for PStance or twitter_stance_kemlm datasets). Defaults to None.
        examples_count (int): Number of examples to use for few-shot prompts (default is 3).
    """
    # Dynamically construct the function name
    function_name = f"{dataset_name}_{model_name}_few_shot_template"

    # Check if the function exists and get the reference
    try:
        prompt_function = globals()[function_name]
    except KeyError:
        raise ValueError(f"Function '{function_name}' does not exist. Ensure it is imported correctly.")

    # Identify example and test files based on dataset
    if dataset_name in ["PStance", "twitter_stance_kemlm"]:
        if not candidate_name:
            raise ValueError(f"Candidate name must be specified for {dataset_name}.")

        example_files = [
            os.path.join(dataset_dir, f) for f in os.listdir(dataset_dir)
            if ("val" if dataset_name == "PStance" else "train") in f.lower() and
            (candidate_name.lower() in f.lower() if candidate_name else True)
        ]

        test_files = [
            os.path.join(dataset_dir, f) for f in os.listdir(dataset_dir)
            if "test" in f.lower() and
            (candidate_name.lower() in f.lower() if candidate_name else True)
        ]

        if not example_files or not test_files:
            raise ValueError(f"No matching files found for candidate '{candidate_name}' in {dataset_dir}.")
    else:
        # Handle other datasets like semeval2016
        example_files = [os.path.join(dataset_dir, f) for f in os.listdir(dataset_dir) if "train" in f.lower()]
        test_files = [os.path.join(dataset_dir, f) for f in os.listdir(dataset_dir) if "test" in f.lower()]

        if not example_files or not test_files:
            raise ValueError(f"Train or test files missing in {dataset_dir} for {dataset_name}.")

    # Select random examples for few-shot prompts
    examples = []
    for example_file in example_files:
        # Determine the delimiter based on file extension
        file_extension = os.path.splitext(example_file)[1].lower()
        if file_extension == ".tsv":
            delimiter = "\t"
        elif file_extension == ".csv":
            delimiter = ","
        else:
            raise ValueError("Unsupported file format. Only CSV and TSV files are supported.")

        with open(example_file, newline='', encoding="unicode_escape") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=delimiter)
            field_mapping = {key.lower(): key for key in reader.fieldnames}
            tweet_col = field_mapping.get("tweet")
            target_col = field_mapping.get("target")
            label_col = field_mapping.get("stance")

            if not tweet_col or not target_col or not label_col:
                raise ValueError(f"{example_file} must contain 'tweet', 'target', and 'stance' columns.")

            rows = [row for row in reader]
            if len(rows) < examples_count:
                raise ValueError(f"{example_file} must have at least {examples_count} rows.")

            # Randomly sample examples
            selected_rows = random.sample(rows, examples_count)
            examples.extend([
                {
                    "tweet": row[tweet_col],
                    "target": row[target_col],
                    "label": row[label_col],
                }
                for row in selected_rows
            ])
        break  # Use only the first matching file for examples

    # Generate prompts from test files
    prompts = []
    for test_file in test_files:
        # Determine the delimiter based on file extension
        file_extension = os.path.splitext(test_file)[1].lower()
        if file_extension == ".tsv":
            delimiter = "\t"
        elif file_extension == ".csv":
            delimiter = ","
        else:
            raise ValueError("Unsupported file format. Only CSV and TSV files are supported.")

        with open(test_file, newline='', encoding="unicode_escape") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=delimiter)
            field_mapping = {key.lower(): key for key in reader.fieldnames}
            tweet_col = field_mapping.get("tweet")
            target_col = field_mapping.get("target")

            if not tweet_col or not target_col:
                raise ValueError(f"{test_file} must contain 'tweet' and 'target' columns.")

            for row in reader:
                tweet = row.get(tweet_col)
                target = row.get(target_col)

                if not tweet or not target:
                    raise ValueError("Invalid data: Missing tweet or target in a row.")

                # Generate the prompt
                prompt = prompt_function(tweet, target, examples)

                # Add to the prompts list with metadata
                prompts.append({
                    "dataset": dataset_name,
                    "model": model_name,
                    "candidate": candidate_name,
                    "tweet": tweet,
                    "target": target,
                    "prompt": prompt,
                })

    # Determine subdirectory based on the type of prompt
    prompt_type = "zero_shot" if "zero_shot" in function_name else "few_shot"
    output_dir = os.path.join(output_dir, prompt_type)

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Construct output file name dynamically
    if dataset_name == "semeval2016":
        output_file = f"{output_dir}/{dataset_name}_{model_name}_few_shot_prompts.json"
    else:
        output_file = f"{output_dir}/{dataset_name}_{model_name}_{candidate_name}_few_shot_prompts.json"

    # Write the prompts to a JSON file
    with open(output_file, "w", encoding="utf-8") as jsonfile:
        json.dump(prompts, jsonfile, indent=4, ensure_ascii=False)

    print(f"Few-shot prompts successfully generated and saved to {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Few-Shot Prompts")
    parser.add_argument("--dataset_dir", type=str, required=True, help="Directory containing the dataset files")
    parser.add_argument("--output_dir", type=str, required=True, help="Directory where the output JSON will be saved")
    parser.add_argument("--dataset_name", type=str, required=True, help="Name of the dataset (e.g., 'PStance')")
    parser.add_argument("--model_name", type=str, required=True, help="Name of the model (e.g., 'qwen2')")
    parser.add_argument("--candidate_name", type=str, default=None, help="Candidate name (e.g., 'bernie')")
    parser.add_argument("--examples_count", type=int, default=3, help="Number of examples to use for few-shot prompts")

    args = parser.parse_args()

    generate_few_shot_prompts(
        dataset_dir=args.dataset_dir,
        output_dir=args.output_dir,
        dataset_name=args.dataset_name,
        model_name=args.model_name,
        candidate_name=args.candidate_name,
        examples_count=args.examples_count,
    )
