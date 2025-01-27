# General utility functions for the project

# Package imports
import json
import os
import re


# Functions
def create_file_list(path: str, indicators_pos: list = [], indicators_neg: list = [], sort: callable = None):
    """Gets all files in a directory according to the indicators"""
                
    # create condition based on all indicators
    condition_pos = lambda x: all([indicator in x for indicator in indicators_pos])
    condition_neg = lambda x: all([indicator not in x for indicator in indicators_neg])
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if condition_pos(file) and condition_neg(file):
                file_list.append(os.path.join(root, file))
    return file_list


def load_json(filepath: str):
    """Loads a json file"""
    
    with open(filepath, "r") as file:
        data = json.load(file)
    return data


def read_files_to_dict(path_dict: dict) -> dict:
    """Replaces a dictionary of file paths with a dictionary of file contents."""
    for key, path in path_dict.items():
        with open(path) as f:
            path_dict[key] = f.read()
    return path_dict


def load_jsonified_resources(week: int, resources_path: str = "resources", keys: list = ["questions", "rubrics", "solutions", "goals"]) -> dict:
    """Loads jsonified questions, rubrics, solutions, and learning goals for a given week."""
    base_path = f"{resources_path}/week-{week}/json/week-{week}"
    jsonified_resources = {}
    for key in keys:
        jsonified_resources[key] = json.load(open(f"{base_path}_{key}.json"))
        jsonified_resources[key] = {k: "\n".join(v) for k, v in jsonified_resources[key].items()}   
    return jsonified_resources 


def deduplicate_highest_attempt(file_paths):
    """Finds the highest attempt for each unique file and returns the list of file paths with the highest attempt"""
    # Dictionary to store the highest attempt for each unique submission
    submission_dict = {}

    for path in file_paths:
        # Extract the unique key and the attempt number using regex
        match = re.search(r'(.*_try-)(\d+)(.*)', path)
        if match:
            base_key = match.group(1) + match.group(3)  # Unique key without the attempt number
            attempt_number = int(match.group(2))  # Extract the attempt number
            
            # Keep the path with the highest attempt
            if base_key not in submission_dict or attempt_number > submission_dict[base_key][1]:
                submission_dict[base_key] = (path, attempt_number)

    # Return the list of file paths with the highest attempt
    return [value[0] for value in submission_dict.values()]