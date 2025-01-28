# General utility functions for the project

# Package imports
import json
import os
import re
import yaml


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

def load_settings_to_globals(settings_path, week_nr) -> None:
    """Loads the settings to set global variables"""
    # Load settings
    with open(settings_path) as f:
            settings = yaml.safe_load(f)

    # Week
    global WEEK_NUMBER 
    global WEEK
    WEEK_NUMBER = week_nr
    WEEK = settings["weeks"][week_nr]

    # Canvas settings
    global COURSE_ID
    global ASSIGNMENT_ID
    global QUIZ_ID
    global R_QUIZ_QUESTION_ID
    global ADV_QUIZ_QUESTION_ID
    global LOCK_GRADES_DATE
    COURSE_ID = settings["global"]["canvas"]["course_id"]
    ASSIGNMENT_ID = WEEK["canvas"]["assignment_id"]
    QUIZ_ID = WEEK["canvas"]["quiz_id"]
    R_QUIZ_QUESTION_ID = WEEK["canvas"]["r_quiz_question_id"]
    ADV_QUIZ_QUESTION_ID = WEEK["canvas"]["adv_quiz_question_id"]
    LOCK_GRADES_DATE = WEEK["lock_grades_date"]


    # LLM Settings
    global MODEL
    global GRADING_TEMPERATURE
    global FEEDBACK_TEMPERATURE
    global N_CHOICES_GRADING
    global N_CHOICES_FEEDBACK
    global PROMPTS
    MODEL = settings["global"]["llm"]["model"]
    GRADING_TEMPERATURE = settings["global"]["llm"]["grading_temperature"]
    FEEDBACK_TEMPERATURE = settings["global"]["llm"]["feedback_temperature"]
    N_CHOICES_GRADING = settings["global"]["llm"]["n_choices_grading"]
    N_CHOICES_FEEDBACK = settings["global"]["llm"]["n_choices_feedback"]
    PROMPTS = {k: read_files_to_dict(settings["global"]["llm"]["prompts"][k]) for k in settings["global"]["llm"]["prompts"].keys()}
    
    # Paths
    global RESOURCES_PATH
    global SUBMISSIONS_PATH
    global STUDENT_SUBMISSION_TEMPLATE
    global STUDENT_SUBMISSION_JSON_TEMPLATE
    global LLM_COMPLETION_REPORT_TEMPLATE
    global LLM_FEEDBACK_REPORT_TEMPLATE
    global LLM_GRADING_REPORT_TEMPLATE
    RESOURCES_PATH = settings["global"]["paths"]["resources"]
    SUBMISSIONS_PATH = settings["global"]["paths"]["submissions"]
    STUDENT_SUBMISSION_TEMPLATE = settings["global"]["paths"]["student_submission_template"]
    STUDENT_SUBMISSION_JSON_TEMPLATE = settings["global"]["paths"]["student_submission_json_template"]
    LLM_COMPLETION_REPORT_TEMPLATE = settings["global"]["paths"]["llm_completion_report_template"]
    LLM_FEEDBACK_REPORT_TEMPLATE = settings["global"]["paths"]["llm_feedback_report_template"]
    LLM_GRADING_REPORT_TEMPLATE = settings["global"]["paths"]["llm_grading_report_template"]

    # Randomization 
    global GROUPS
    global SEED
    GROUPS = settings["global"]["randomization"]["groups"]
    SEED = settings["global"]["randomization"]["seed"]

    # Surveys
    global SURVEY_QUESTIONS
    global SURVEY_DEFINITIONS
    SURVEY_QUESTIONS = settings["surveys"]["survey_questions"]
    SURVEY_DEFINITIONS = settings["surveys"]["survey_definitions"]
