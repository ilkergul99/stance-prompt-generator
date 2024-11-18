"""
@author:  İlker Gül
@contact: ilker.gul@epfl.ch
"""

########  Zero shot and few-shot templates  ########

def semeval2016_zero_shot_template(tweet: str, target: str) -> str:
    prompt = (
        "Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n"
        "### Instruction:\n"
        "You are an expert assistant specializing in stance detection. Your task is to determine the stance expressed "
        f"in the following tweet towards the target: \"{target}\".\n\n"
        "Stance detection involves identifying whether the tweet expresses one of the following stances:\n"
        "- **support**: The tweet shows a positive or supportive attitude towards the target, either explicitly or implicitly.\n"
        "- **against**: The tweet expresses opposition or criticism towards the target, either explicitly or implicitly.\n"
        "- **none**: The tweet is neutral, unrelated, or does not express any stance towards the target.\n\n"
        "To determine the stance, consider the following factors:\n"
        "- Explicit statements or opinions in the text.\n"
        "- Subtext, cultural or regional references.\n"
        "- Implicit meanings or attitudes suggested by the content.\n\n"
        f"Tweet: \"{tweet}\"\n\n"
        "### Question:\n"
        f'What is the stance of this tweet towards the target "{target}"?\n'
        "Choose one of the following options: support, against, none.\n\n"
        "### Answer:"
    )
    return prompt


def semeval2016_few_shot_template(tweet: str, target: str, examples: list) -> str:
    # Construct few-shot examples
    few_shot_examples = "\n\n".join(
        f"Example {i + 1}:\n"
        f"Tweet: \"{example['tweet']}\"\n"
        f"Target: \"{example['target']}\"\n"
        f"Stance: {example['label']}"
        for i, example in enumerate(examples)
    )

    # Combine examples with the main prompt
    prompt = (
        "Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n"
        "### Instruction:\n"
        "You are an expert assistant specializing in stance detection. Your task is to determine the stance expressed "
        f"in the following tweet towards the target: \"{target}\".\n\n"
        "Stance detection involves identifying whether the tweet expresses one of the following stances:\n"
        "- **support**: The tweet shows a positive or supportive attitude towards the target, either explicitly or implicitly.\n"
        "- **against**: The tweet expresses opposition or criticism towards the target, either explicitly or implicitly.\n"
        "- **none**: The tweet is neutral, unrelated, or does not express any stance towards the target.\n\n"
        "To determine the stance, consider the following factors:\n"
        "- Explicit statements or opinions in the text.\n"
        "- Subtext, cultural or regional references.\n"
        "- Implicit meanings or attitudes suggested by the content.\n\n"
        "Here are some examples for guidance:\n\n"
        f"{few_shot_examples}\n\n"
        "Now, analyze the following tweet:\n\n"
        f"Tweet: \"{tweet}\"\n\n"
        "### Question:\n"
        f'What is the stance of this tweet towards the target "{target}"?\n'
        "Choose one of the following options: support, against, none.\n\n"
        "### Answer:"
    )
    return prompt


###### SemEVAL-2016 LLAMA-2 ###### 
def semeval2016_llama2_zero_shot_template(tweet: str, target: str) -> str:
    prompt = (
        "[INST] <<SYS>>\n"
        "You are an expert assistant for stance detection. "
        f"Your task is to determine the stance expressed in the following tweet towards the target: \"{target}\".\n\n"
        "Stance detection involves identifying whether the tweet expresses one of the following stances:\n"
        "- **support**: The tweet shows a positive or supportive attitude towards the target, either explicitly or implicitly.\n"
        "- **against**: The tweet expresses opposition or criticism towards the target, either explicitly or implicitly.\n"
        "- **none**: The tweet is neutral, unrelated, or does not express any stance towards the target.\n\n"
        "To make your assessment, consider the following factors:\n"
        "- Explicit statements or opinions in the text.\n"
        "- Subtext, cultural or regional references.\n"
        "- Implicit meanings or attitudes suggested by the content.\n\n"
        "Please analyze the tweet carefully and provide a classification from the possible stances.\n"
        "<</SYS>>\n\n"
        f"Tweet: \"{tweet}\"\n\n"
        f"What is the stance of this tweet towards \"{target}\"? Choose one: support, against, none.\n"
        "[/INST]"
    )
    return prompt


def semeval2016_llama2_few_shot_template(tweet: str, target: str, examples: list) -> str:
    # Construct few-shot examples
    few_shot_examples = "\n\n".join(
        f"Example {i + 1}:\n"
        f"Tweet: \"{example['tweet']}\"\n"
        f"Target: \"{example['target']}\"\n"
        f"Stance: {example['label']}"
        for i, example in enumerate(examples)
    )

    # Combine examples with the main prompt
    prompt = (
        "[INST] <<SYS>>\n"
        "You are an expert assistant for stance detection. "
        f"Your task is to determine the stance expressed in the following tweet towards the target: \"{target}\".\n\n"
        "Stance detection involves identifying whether the tweet expresses one of the following stances:\n"
        "- **support**: The tweet shows a positive or supportive attitude towards the target, either explicitly or implicitly.\n"
        "- **against**: The tweet expresses opposition or criticism towards the target, either explicitly or implicitly.\n"
        "- **none**: The tweet is neutral, unrelated, or does not express any stance towards the target.\n\n"
        "To make your assessment, consider the following factors:\n"
        "- Explicit statements or opinions in the text.\n"
        "- Subtext, cultural or regional references.\n"
        "- Implicit meanings or attitudes suggested by the content.\n\n"
        "Here are some examples for guidance:\n\n"
        f"{few_shot_examples}\n\n"
        "Now, analyze the following tweet:\n\n"
        f"Tweet: \"{tweet}\"\n\n"
        f"What is the stance of this tweet towards \"{target}\"? Choose one: support, against, none.\n"
        "[/INST]"
    )
    return prompt


###### SemEVAL-2016 MISTRAL ###### 
def semeval2016_mistral_zero_shot_template(tweet: str, target: str) -> str:
    prompt = (
        "[INST] "
        "You are an expert assistant specializing in stance detection. "
        f"Your task is to determine the stance expressed in the following tweet towards the target: \"{target}\".\n\n"
        "Stance detection involves identifying whether the tweet expresses one of the following attitudes:\n"
        "- **support**: The tweet shows a positive or supportive attitude towards the target, explicitly or implicitly.\n"
        "- **against**: The tweet expresses opposition or criticism towards the target, explicitly or implicitly.\n"
        "- **none**: The tweet is neutral, unrelated, or does not express any stance towards the target.\n\n"
        "Analyze the tweet carefully, considering the following:\n"
        "- Explicit statements in the text.\n"
        "- Subtext, cultural or regional references.\n"
        "- Implicit meanings that may not be directly stated but suggest a stance.\n\n"
        f"Tweet: \"{tweet}\"\n\n"
        f"What is the stance of this tweet towards \"{target}\"? Choose one: support, against, none.\n"
        "[/INST]"
    )
    return prompt


def semeval2016_mistral_few_shot_template(tweet: str, target: str, examples: list) -> str:
    # Construct few-shot examples
    few_shot_examples = "\n\n".join(
        f"Example {i + 1}:\n"
        f"Tweet: \"{example['tweet']}\"\n"
        f"Target: \"{example['target']}\"\n"
        f"Stance: {example['label']}"
        for i, example in enumerate(examples)
    )

    # Combine examples with the main prompt
    prompt = (
        "[INST] "
        "You are an expert assistant specializing in stance detection. "
        f"Your task is to determine the stance expressed in the following tweet towards the target: \"{target}\".\n\n"
        "Stance detection involves identifying whether the tweet expresses one of the following attitudes:\n"
        "- **support**: The tweet shows a positive or supportive attitude towards the target, explicitly or implicitly.\n"
        "- **against**: The tweet expresses opposition or criticism towards the target, explicitly or implicitly.\n"
        "- **none**: The tweet is neutral, unrelated, or does not express any stance towards the target.\n\n"
        "Analyze the tweet carefully, considering the following:\n"
        "- Explicit statements in the text.\n"
        "- Subtext, cultural or regional references.\n"
        "- Implicit meanings that may not be directly stated but suggest a stance.\n\n"
        "Here are some examples for guidance:\n\n"
        f"{few_shot_examples}\n\n"
        "Now, analyze the following tweet:\n\n"
        f"Tweet: \"{tweet}\"\n\n"
        f"What is the stance of this tweet towards \"{target}\"? Choose one: support, against, none.\n"
        "[/INST]"
    )
    return prompt


###### SemEVAL-2016 Qwen 2 ######
def semeval2016_qwen2_zero_shot_template(tweet: str, target: str) -> str:
    prompt = (
        "<|im_start|>system\n"
        "You are an expert assistant specializing in stance detection. Your task is to determine the stance expressed "
        "in a given tweet towards a specified target.\n\n"
        "Stance detection involves identifying whether the tweet expresses one of the following stances:\n"
        "- **support**: The tweet shows a positive or supportive attitude towards the target, either explicitly or implicitly.\n"
        "- **against**: The tweet expresses opposition or criticism towards the target, either explicitly or implicitly.\n"
        "- **none**: The tweet is neutral, unrelated, or does not express any stance towards the target.\n\n"
        "To determine the stance, consider the following factors:\n"
        "- Explicit statements or opinions in the text.\n"
        "- Subtext, cultural or regional references.\n"
        "- Implicit meanings or attitudes suggested by the content.\n\n"
        "Analyze the tweet carefully and classify its stance as one of the above options.\n"
        "<|im_end|>\n"
        "<|im_start|>user\n"
        f"Tweet: \"{tweet}\"\n\n"
        f"Target: \"{target}\"\n\n"
        "What is the stance of this tweet towards the target? Choose one: support, against, none.\n"
        "<|im_end|>\n"
    )
    return prompt


def semeval2016_qwen2_few_shot_template(tweet: str, target: str, examples: list) -> str:
    # Construct the few-shot examples in Qwen format
    few_shot_examples = "\n\n".join(
        "<|im_start|>user\n"
        f"Tweet: \"{example['tweet']}\"\n\n"
        f"Target: \"{example['target']}\"\n\n"
        "What is the stance of this tweet towards the target? Choose one: support, against, none.\n"
        "<|im_end|>\n"
        "<|im_start|>assistant\n"
        f"{example['label']}\n"
        "<|im_end|>"
        for example in examples
    )

    # Full prompt with the examples and main task
    prompt = (
        "<|im_start|>system\n"
        "You are an expert assistant specializing in stance detection. Your task is to determine the stance expressed "
        f"in a given tweet towards a specified target: \"{target}\".\n\n"
        "Stance detection involves identifying whether the tweet expresses one of the following stances:\n"
        "- **support**: The tweet shows a positive or supportive attitude towards the target, either explicitly or implicitly.\n"
        "- **against**: The tweet expresses opposition or criticism towards the target, either explicitly or implicitly.\n"
        "- **none**: The tweet is neutral, unrelated, or does not express any stance towards the target.\n\n"
        "To determine the stance, consider the following factors:\n"
        "- Explicit statements or opinions in the text.\n"
        "- Subtext, cultural or regional references.\n"
        "- Implicit meanings or attitudes suggested by the content.\n\n"
        "Analyze the tweet carefully and classify its stance as one of the above options.\n"
        "<|im_end|>\n\n"
        f"{few_shot_examples}\n\n"
        "<|im_start|>user\n"
        f"Tweet: \"{tweet}\"\n\n"
        f"Target: \"{target}\"\n\n"
        "What is the stance of this tweet towards the target? Choose one: support, against, none.\n"
        "<|im_end|>\n"
    )
    return prompt


###### TWITTER STANCE ChatGPT, CLAUDE, ETC. ###### 
def twitter_stance_kemlm_zero_shot_template(tweet: str, target: str) -> str:
    prompt = (
        "Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n"
        "### Instruction:\n"
        "You are a helpful and respectful assistant specializing in stance detection. "
        "Your task is to analyze the following tweet and determine its stance towards the given target: "
        f"\"{target}\".\n\n"
        "Stance detection is the process of identifying whether the author of a tweet is:\n"
        "- **support**: Expressing a positive or supportive attitude towards the target, explicitly or implicitly.\n"
        "- **against**: Expressing opposition or criticism towards the target, explicitly or implicitly.\n"
        "- **none**: Neutral, unrelated, or expressing no clear stance towards the target.\n\n"
        "Consider both explicit statements and implicit factors such as subtext, cultural references, and regional nuances.\n\n"
        f"Tweet: \"{tweet}\"\n\n"
        "### Question:\n"
        f'What is the stance of this tweet towards the target "{target}"?\n'
        "Choose one of the following options: support, against, none.\n\n"
        "### Answer:"
    )
    return prompt


def twitter_stance_kemlm_few_shot_template(tweet: str, target: str, examples: list) -> str:
    # Construct few-shot examples
    few_shot_examples = "\n\n".join(
        f"Example {i + 1}:\n"
        f"Tweet: \"{example['tweet']}\"\n"
        f"Target: \"{example['target']}\"\n"
        f"Stance: {example['label']}"
        for i, example in enumerate(examples)
    )

    # Combine examples with the main prompt
    prompt = (
        "Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n"
        "### Instruction:\n"
        "You are a helpful and respectful assistant specializing in stance detection. "
        "Your task is to analyze the following tweet and determine its stance towards the given target: "
        f"\"{target}\".\n\n"
        "Stance detection is the process of identifying whether the author of a tweet is:\n"
        "- **support**: Expressing a positive or supportive attitude towards the target, explicitly or implicitly.\n"
        "- **against**: Expressing opposition or criticism towards the target, explicitly or implicitly.\n"
        "- **none**: Neutral, unrelated, or expressing no clear stance towards the target.\n\n"
        "Consider both explicit statements and implicit factors such as subtext, cultural references, and regional nuances.\n\n"
        "Here are some examples for guidance:\n\n"
        f"{few_shot_examples}\n\n"
        "Now, analyze the following tweet:\n\n"
        f"Tweet: \"{tweet}\"\n\n"
        "### Question:\n"
        f'What is the stance of this tweet towards the target "{target}"?\n'
        "Choose one of the following options: support, against, none.\n\n"
        "### Answer:"
    )
    return prompt



###### TWITTER STANCE LLAMA 2 ###### 
def twitter_stance_kemlm_llama2_zero_shot_template(tweet: str, target: str) -> str:
    prompt = (
        "[INST] <<SYS>>\n"
        "You are an expert assistant specializing in stance detection for a given target. "
        f"Your task is to determine the stance of the following tweet towards the target: \"{target}\".\n\n"
        "Stance detection involves identifying whether the tweet expresses one of the following attitudes:\n"
        "- **support**: The tweet shows a positive or supportive attitude towards the target, explicitly or implicitly.\n"
        "- **against**: The tweet expresses opposition or criticism towards the target, explicitly or implicitly.\n"
        "- **none**: The tweet is neutral, unrelated, or does not express any stance towards the target.\n\n"
        "Consider the following factors when analyzing the tweet:\n"
        "- Explicit statements or opinions in the text.\n"
        "- Subtext, cultural or regional references.\n"
        "- Implicit meanings that suggest a stance, even if not directly stated.\n\n"
        "Please analyze the tweet thoroughly and provide your answer.\n"
        "<</SYS>>\n\n"
        f"Tweet: \"{tweet}\"\n\n"
        f"Stance towards \"{target}\": [/INST]"
    )
    return prompt


def twitter_stance_kemlm_llama2_few_shot_template(tweet: str, target: str, examples: list) -> str:
    # Construct few-shot examples
    few_shot_examples = "\n\n".join(
        f"Example {i + 1}:\n"
        f"Tweet: \"{example['tweet']}\"\n"
        f"Target: \"{example['target']}\"\n"
        f"Stance: {example['label']}"
        for i, example in enumerate(examples)
    )

    # Combine examples with the main prompt
    prompt = (
        "[INST] <<SYS>>\n"
        "You are an expert assistant specializing in stance detection for a given target. "
        f"Your task is to determine the stance of the following tweet towards the target: \"{target}\".\n\n"
        "Stance detection involves identifying whether the tweet expresses one of the following attitudes:\n"
        "- **support**: The tweet shows a positive or supportive attitude towards the target, explicitly or implicitly.\n"
        "- **against**: The tweet expresses opposition or criticism towards the target, explicitly or implicitly.\n"
        "- **none**: The tweet is neutral, unrelated, or does not express any stance towards the target.\n\n"
        "Consider the following factors when analyzing the tweet:\n"
        "- Explicit statements or opinions in the text.\n"
        "- Subtext, cultural or regional references.\n"
        "- Implicit meanings that suggest a stance, even if not directly stated.\n\n"
        "Here are some examples for guidance:\n\n"
        f"{few_shot_examples}\n\n"
        "Now, analyze the following tweet:\n\n"
        f"Tweet: \"{tweet}\"\n\n"
        f"Stance towards \"{target}\": [/INST]"
    )
    return prompt


###### TWITTER STANCE MISTRAL ###### 
def twitter_stance_kemlm_mistral_zero_shot_template(tweet: str, target: str) -> str:
    prompt = (
        "[INST] "
        "You are a highly capable assistant specializing in detecting the stance expressed in tweets about a specific target. "
        f"The target in question is: \"{target}\".\n\n"
        "Stance detection is the task of determining whether a tweet expresses one of the following attitudes toward the target:\n"
        "- **support**: The tweet expresses a positive or supportive attitude toward the target, either explicitly or implicitly.\n"
        "- **against**: The tweet expresses opposition or criticism toward the target, either explicitly or implicitly.\n"
        "- **none**: The tweet is neutral, unrelated, or does not take any clear stance toward the target.\n\n"
        "Your task is to carefully analyze the tweet and classify its stance toward the target. This may require understanding:\n"
        "- Explicit content within the text (e.g., direct statements or opinions).\n"
        "- Subtext, cultural references, or regional nuances.\n"
        "- Implicit meanings that may not be directly stated but suggest a stance.\n\n"
        f"Here is the tweet for analysis:\n\n"
        f"Tweet: \"{tweet}\"\n\n"
        "### Question:\n"
        f'What is the stance of this tweet toward the target "{target}"?\n'
        "Choose one of the following options: support, against, none.\n\n"
        "### Answer:"
    )
    return prompt


def twitter_stance_kemlm_mistral_few_shot_template(tweet: str, target: str, examples: list) -> str:
    # Construct the few-shot examples
    few_shot_examples = "\n\n".join(
        f"Example {i + 1}:\n"
        f"Tweet: \"{example['tweet']}\"\n"
        f"Target: \"{example['target']}\"\n"
        f"Stance: {example['label']}"
        for i, example in enumerate(examples)
    )
    
    # Combine examples with the main prompt
    prompt = (
        "[INST] "
        "You are a highly capable assistant specializing in detecting the stance expressed in tweets about a specific target. "
        f"The target in question is: \"{target}\".\n\n"
        "Stance detection is the task of determining whether a tweet expresses one of the following attitudes toward the target:\n"
        "- **support**: The tweet expresses a positive or supportive attitude toward the target, either explicitly or implicitly.\n"
        "- **against**: The tweet expresses opposition or criticism toward the target, either explicitly or implicitly.\n"
        "- **none**: The tweet is neutral, unrelated, or does not take any clear stance toward the target.\n\n"
        "Your task is to analyze the tweet carefully and classify its stance toward the target. This may require understanding:\n"
        "- Explicit content within the text (e.g., direct statements or opinions).\n"
        "- Subtext, cultural references, or regional nuances.\n"
        "- Implicit meanings that may not be directly stated but suggest a stance.\n\n"
        "Here are some examples for guidance:\n\n"
        f"{few_shot_examples}\n\n"
        "Now, analyze the following tweet:\n\n"
        f"Tweet: \"{tweet}\"\n\n"
        "### Question:\n"
        f'What is the stance of this tweet toward the target "{target}"?\n'
        "Choose one of the following options: support, against, none.\n\n"
        "### Answer:"
    )
    return prompt


###### TWITTER STANCE QWEN 2 ###### 
def twitter_stance_kemlm_qwen2_zero_shot_template(tweet: str, target: str) -> str:
    prompt = (
        "<|im_start|>system\n"
        "You are an expert assistant specializing in stance detection. Your task is to analyze the given tweet and "
        f"determine its stance towards the specified target: \"{target}\".\n\n"
        "Stance detection involves identifying whether the tweet expresses one of the following stances:\n"
        "- **support**: The tweet shows a positive or supportive attitude towards the target, explicitly or implicitly.\n"
        "- **against**: The tweet expresses opposition or criticism towards the target, explicitly or implicitly.\n"
        "- **none**: The tweet is neutral, unrelated, or does not express any stance towards the target.\n\n"
        "Consider the following factors in your analysis:\n"
        "- Explicit statements or opinions in the text.\n"
        "- Subtext, cultural or regional references.\n"
        "- Implicit meanings or attitudes suggested by the content.\n"
        "<|im_end|>\n"
        "<|im_start|>user\n"
        f"Tweet: \"{tweet}\"\n\n"
        f"Target: \"{target}\"\n\n"
        "What is the stance of this tweet towards the target? Choose one: support, against, none.\n"
        "<|im_end|>\n"
    )
    return prompt

def twitter_stance_kemlm_qwen2_few_shot_template(tweet: str, target: str, examples: list) -> str:
    # Construct few-shot examples in Qwen format
    few_shot_examples = "\n\n".join(
        "<|im_start|>user\n"
        f"Tweet: \"{example['tweet']}\"\n\n"
        f"Target: \"{example['target']}\"\n\n"
        "What is the stance of this tweet towards the target? Choose one: support, against, none.\n"
        "<|im_end|>\n"
        "<|im_start|>assistant\n"
        f"{example['label']}\n"
        "<|im_end|>"
        for example in examples
    )

    # Combine examples with the main task
    prompt = (
        "<|im_start|>system\n"
        "You are an expert assistant specializing in stance detection. Your task is to analyze the given tweet and "
        f"determine its stance towards the specified target: \"{target}\".\n\n"
        "Stance detection involves identifying whether the tweet expresses one of the following stances:\n"
        "- **support**: The tweet shows a positive or supportive attitude towards the target, explicitly or implicitly.\n"
        "- **against**: The tweet expresses opposition or criticism towards the target, explicitly or implicitly.\n"
        "- **none**: The tweet is neutral, unrelated, or does not express any stance towards the target.\n\n"
        "Consider the following factors in your analysis:\n"
        "- Explicit statements or opinions in the text.\n"
        "- Subtext, cultural or regional references.\n"
        "- Implicit meanings or attitudes suggested by the content.\n"
        "<|im_end|>\n\n"
        f"{few_shot_examples}\n\n"
        "<|im_start|>user\n"
        f"Tweet: \"{tweet}\"\n\n"
        f"Target: \"{target}\"\n\n"
        "What is the stance of this tweet towards the target? Choose one: support, against, none.\n"
        "<|im_end|>\n"
    )
    return prompt


###### P-STANCE CHATGPT, CLAUDE, ETC. ######    
def PStance_zero_shot_template(tweet: str, target: str) -> str:
    prompt = (
        "You are an expert assistant for stance detection in U.S. political tweets. "
        "Your task is to determine the stance expressed in the given tweet towards the target: "
        f"\"{target}\".\n\n"
        "Stance detection identifies whether the tweet supports or opposes the target. Analyze the tweet carefully, "
        "considering explicit statements, subtext, cultural or regional references, and implicit meanings.\n\n"
        "Possible stances:\n"
        "- support: The tweet shows a positive or supportive attitude towards the target.\n"
        "- against: The tweet opposes or criticizes the target.\n\n"
        f"Tweet: \"{tweet}\"\n\n"
        f"What is the stance of this tweet towards \"{target}\"? Choose one: support, against.\n\n"
        "Answer:"
    )
    return prompt

def PStance_few_shot_template(tweet: str, target: str, examples: list) -> str:
    # Construct few-shot examples
    few_shot_examples = "\n".join(
        f"Example {i + 1}:\n"
        f"Tweet: \"{example['tweet']}\"\n"
        f"Target: \"{example['target']}\"\n"
        f"Stance: {example['label']}\n"
        for i, example in enumerate(examples)
    )
    
    # Full prompt with few-shot examples
    prompt = (
        "You are an expert assistant for stance detection in U.S. political tweets. "
        "Your task is to determine the stance expressed in the given tweet towards the target: "
        f"\"{target}\".\n\n"
        "Stance detection identifies whether the tweet supports or opposes the target. Analyze the tweet carefully, "
        "considering explicit statements, subtext, cultural or regional references, and implicit meanings.\n\n"
        "Possible stances:\n"
        "- support: The tweet shows a positive or supportive attitude towards the target.\n"
        "- against: The tweet opposes or criticizes the target.\n\n"
        "Here are some examples:\n\n"
        f"{few_shot_examples}\n\n"
        f"Now analyze the following tweet:\n\n"
        f"Tweet: \"{tweet}\"\n\n"
        f"What is the stance of this tweet towards \"{target}\"? Choose one: support, against.\n\n"
        "Answer:"
    )
    return prompt


###### P-STANCE LLAMA-2 ######
def PStance_llama2_zero_shot_template(tweet: str, target: str) -> str:
    prompt = (
        "[INST] <<SYS>> "
        "You are an assistant specializing in stance detection for political tweets "
        f"about U.S. presidential candidates. Your task is to analyze the given tweet "
        f"and determine its stance towards the target: \"{target}\".\n\n"
        "Stance detection involves identifying whether the author of a tweet is in favor of "
        "or against a target. This may include understanding subtext, cultural or regional references, "
        "and implicit meanings.\n\n"
        "Possible stances:\n"
        "- support: The tweet shows a positive or supportive attitude towards the target, explicitly or implicitly.\n"
        "- against: The tweet criticizes or opposes the target, explicitly or implicitly.\n"
        "<</SYS>>\n\n"
        f"Tweet: \"{tweet}\"\n"
        f'Stance towards "{target}": [/INST]'
    )
    return prompt


def PStance_llama2_few_shot_template(tweet: str, target: str, examples: list) -> str:
    # Prepare few-shot examples as readable entries
    few_shot_examples = "\n".join(
        f"Example {i + 1}:\n"
        f"Tweet: \"{example['tweet']}\"\n"
        f"Target: \"{example['target']}\"\n"
        f"Stance: {example['label']}\n"
        for i, example in enumerate(examples)
    )
    
    # Combine examples with the main prompt
    prompt = (
        "[INST] <<SYS>> "
        "You are an assistant specializing in stance detection for political tweets "
        f"about U.S. presidential candidates. Your task is to analyze the given tweet "
        f"and determine its stance towards the target: \"{target}\".\n\n"
        "Stance detection involves identifying whether the author of a tweet is in favor of "
        "or against a target. This may include understanding subtext, cultural or regional references, "
        "and implicit meanings.\n\n"
        "Possible stances:\n"
        "- support: The tweet shows a positive or supportive attitude towards the target, explicitly or implicitly.\n"
        "- against: The tweet criticizes or opposes the target, explicitly or implicitly.\n"
        "<</SYS>>\n\n"
        "Here are some examples:\n\n"
        f"{few_shot_examples}\n\n"
        f"Now analyze the following tweet:\n\n"
        f"Tweet: \"{tweet}\"\n"
        f'Stance towards "{target}": [/INST]'
    )
    return prompt


###### P-STANCE MISTRAL ######

def PStance_mistral_zero_shot_template(tweet: str, target: str) -> str:
    prompt = (
        "[INST] "
        "You are an assistant specializing in stance detection for political tweets "
        "about U.S. presidential candidates. Your task is to determine whether a tweet "
        f"is 'support' or 'against' the target: \"{target}\".\n\n"
        "Stance detection involves understanding both explicit statements and implicit subtext, "
        "including cultural or regional references. The possible stances are:\n"
        "- support: The tweet shows a positive or supportive attitude toward the target.\n"
        "- against: The tweet opposes or criticizes the target.\n\n"
        f"Analyze the following tweet carefully:\n\n"
        f"Tweet: \"{tweet}\"\n"
        f'Stance towards "{target}": [/INST]'
    )
    return prompt


def PStance_mistral_few_shot_template(tweet: str, target: str, examples: list) -> str:
    # Prepare few-shot examples as readable explanations
    few_shot_examples = "\n".join(
        f"Example {i + 1}:\n"
        f"Tweet: \"{example['tweet']}\"\n"
        f"Target: \"{example['target']}\"\n"
        f"Stance: {example['label']}\n"
        for i, example in enumerate(examples)
    )
    
    # Combine examples with the main prompt
    prompt = (
        "[INST] "
        "You are an assistant specializing in stance detection for political tweets "
        "about U.S. presidential candidates. Your task is to determine whether a tweet "
        f"is 'support' or 'against' the target: \"{target}\".\n\n"
        "Stance detection involves understanding both explicit statements and implicit subtext, "
        "including cultural or regional references. The possible stances are:\n"
        "- support: The tweet shows a positive or supportive attitude toward the target.\n"
        "- against: The tweet opposes or criticizes the target.\n\n"
        "Here are some examples:\n\n"
        f"{few_shot_examples}\n\n"
        f"Now analyze the following tweet:\n\n"
        f"Tweet: \"{tweet}\"\n"
        f'Stance towards "{target}": [/INST]'
    )
    return prompt


###### P-STANCE QWEN 2 ######
def PStance_qwen2_zero_shot_template(tweet: str, target: str) -> str:
    prompt = (
        "<|im_start|>system\n"
        "You are an expert assistant for stance detection in U.S. political tweets. Your task is to determine the stance expressed "
        f"in the given tweet towards the target: \"{target}\".\n\n"
        "Stance detection involves identifying whether the tweet supports or opposes the target. Analyze the tweet carefully, "
        "considering explicit statements, subtext, cultural or regional references, and implicit meanings.\n\n"
        "Possible stances:\n"
        "- **support**: The tweet shows a positive or supportive attitude towards the target.\n"
        "- **against**: The tweet opposes or criticizes the target.\n"
        "<|im_end|>\n"
        "<|im_start|>user\n"
        f"Tweet: \"{tweet}\"\n\n"
        f"What is the stance of this tweet towards \"{target}\"? Choose one: support, against.\n"
        "<|im_end|>\n"
    )
    return prompt

def PStance_qwen2_few_shot_template(tweet: str, target: str, examples: list) -> str:
    # Construct few-shot examples in Qwen format
    few_shot_examples = "\n\n".join(
        "<|im_start|>user\n"
        f"Tweet: \"{example['tweet']}\"\n\n"
        f"What is the stance of this tweet towards \"{example['target']}\"? Choose one: support, against.\n"
        "<|im_end|>\n"
        "<|im_start|>assistant\n"
        f"{example['label']}\n"
        "<|im_end|>"
        for example in examples
    )

    # Combine examples with the main task
    prompt = (
        "<|im_start|>system\n"
        "You are an expert assistant for stance detection in U.S. political tweets. Your task is to determine the stance expressed "
        f"in the given tweet towards the target: \"{target}\".\n\n"
        "Stance detection involves identifying whether the tweet supports or opposes the target. Analyze the tweet carefully, "
        "considering explicit statements, subtext, cultural or regional references, and implicit meanings.\n\n"
        "Possible stances:\n"
        "- **support**: The tweet shows a positive or supportive attitude towards the target.\n"
        "- **against**: The tweet opposes or criticizes the target.\n"
        "<|im_end|>\n\n"
        f"{few_shot_examples}\n\n"
        "<|im_start|>user\n"
        f"Tweet: \"{tweet}\"\n\n"
        f"What is the stance of this tweet towards \"{target}\"? Choose one: support, against.\n"
        "<|im_end|>\n"
    )
    return prompt
