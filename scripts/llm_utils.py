from collections import defaultdict
from openai import Completion
import pickle as pkl

from scripts.utils import ensure_folder_exists
def create_openai_message(role: str, content: str) -> list:
    return [{"role": role, "content": content}]

def prompt_gpt(openai_client, model, messages, pkl_out_path: str, pkl_this: bool = True, **kwargs) -> Completion:
    # Prompt GPT
    completion = openai_client.chat.completions.create(model=model, 
                                                       messages=messages, 
                                                       **kwargs)
    # Pickle the completion
    if pkl_this:
        ensure_folder_exists(pkl_out_path)
        pkl.dump(completion, open(pkl_out_path, "wb"))

    return completion

def format_with_default(text, formatting_dict, default_value = "<NOT PROVIDED>"):
    return text.format_map(defaultdict(lambda: default_value, formatting_dict))