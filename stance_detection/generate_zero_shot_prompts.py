import os
import csv
import json
import argparse
from prompts import * # Import all your functions


def generate_zero_shot_prompts(input_file: str, output_dir: str, dataset_name: str, model_name: str, candidate_name: str = None):
    """
    Generates zero-shot prompts from a dataset file (CSV or TSV) for the specified dataset and model,
    using appropriate template functions, and stores the results in a JSON file.

    Args:
        input_file (str): Path to the input dataset file (CSV or TSV).
        output_dir (str): Directory where the output JSON file will be saved.
        dataset_name (str): Name of the dataset to use for generating prompts (e.g., "PStance").
        model_name (str): Name of the model to use for generating prompts (e.g., "qwen2").
        candidate_name (str): Optional. Name of the candidate (e.g., "bernie", "biden", "trump").
    
    The input file must contain the following columns:
        - `tweet` or `Tweet`: The tweet text to analyze.
        - `target` or `Target`: The target for stance detection.
    """
    # Dynamically construct the function name
    function_name = f"{dataset_name}_{model_name}_zero_shot_template"

    # Check if the function exists and get the reference
    try:
        prompt_function = globals()[function_name]
    except KeyError:
        raise ValueError(f"Function '{function_name}' does not exist. Ensure it is imported correctly.")

    # Determine the delimiter based on file extension
    file_extension = os.path.splitext(input_file)[1].lower()
    if file_extension == ".tsv":
        delimiter = "\t"
    elif file_extension == ".csv":
        delimiter = ","
    else:
        raise ValueError("Unsupported file format. Only CSV and TSV files are supported.")

    # Read the dataset and generate prompts
    prompts = []
    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=delimiter)
        
        # Normalize column names
        field_mapping = {
            key.lower(): key for key in reader.fieldnames
        }
        tweet_col = field_mapping.get('tweet')
        target_col = field_mapping.get('target')

        if not tweet_col or not target_col:
            raise ValueError(f"The file '{input_file}' must contain 'tweet' or 'Tweet' and 'target' or 'Target' columns.")

        for row in reader:
            tweet = row.get(tweet_col)
            target = row.get(target_col)
            
            if not tweet or not target:
                raise ValueError("Invalid data: Missing tweet or target in a row.")
            
            # Generate the prompt
            prompt = prompt_function(tweet, target)
            
            # Add to the prompts list with metadata
            prompts.append({
                "dataset": dataset_name,
                "model": model_name,
                "candidate": candidate_name,
                "tweet": tweet,
                "target": target,
                "prompt": prompt,
            })

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Construct output file name dynamically
    if candidate_name:
        output_file = f"{output_dir}/{dataset_name}_{model_name}_{candidate_name}_prompts.json"
    else:
        output_file = f"{output_dir}/{dataset_name}_{model_name}_prompts.json"

    # Write the prompts to a JSON file
    with open(output_file, "w", encoding="utf-8") as jsonfile:
        json.dump(prompts, jsonfile, indent=4, ensure_ascii=False)

    print(f"Prompts successfully generated and saved to {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Zero-Shot Prompts")
    parser.add_argument("--input_csv", type=str, required=True, help="Path to the input CSV file")
    parser.add_argument("--output_dir", type=str, required=True, help="Directory where the output JSON will be saved")
    parser.add_argument("--dataset_name", type=str, required=True, help="Name of the dataset (e.g., 'PStance')")
    parser.add_argument("--model_name", type=str, required=True, help="Name of the model (e.g., 'qwen2')")
    parser.add_argument("--candidate_name", type=str, default=None, help="Candidate name (e.g., 'bernie')")

    args = parser.parse_args()

    generate_zero_shot_prompts(
        input_csv=args.input_csv,
        output_dir=args.output_dir,
        dataset_name=args.dataset_name,
        model_name=args.model_name,
        candidate_name=args.candidate_name,
    )


