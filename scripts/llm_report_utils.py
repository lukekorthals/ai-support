import os

def start_report_with_header(report_path: str, model: str, grading_temperature: float, feedback_temperature: float, n_choices_grading: int, n_choices_feedback: int, student_id: int, week: int):
    template = """# LLM Prompt Report
- model: {model}
- grading_temperature: {grading_temperature}
- feedback_temperature: {feedback_temperature}
- n_choices_grading: {n_choices_grading}
- n_choices_feedback: {n_choices_feedback}
- student_id: {student_id}
- week: {week}\n\n"""
    text = template.format(model=model, 
                           grading_temperature=grading_temperature, 
                           feedback_temperature=feedback_temperature, 
                           n_choices_grading=n_choices_grading, 
                           n_choices_feedback=n_choices_feedback, 
                           student_id=student_id, week=week)
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, "w") as f:
        f.write(text)

def add_messages_to_report(report_path: str, messages: list, header: str = "### Messages\n"):
    """Adds messages to a report."""
    template = """<blockquote>
<strong>{role}</strong>

\t{content}
</blockquote>\n\n"""

    text = header
    for message in messages:
        text += template.format(role=message["role"], content="\n\t".join(message["content"].split("\n")))
    with open(report_path, "a") as f:
        f.write(text)

def add_text_to_report(report_path: str, text: str, start_new: bool = False):
    mode = "a"
    if start_new:
        mode = "w"
    with open(report_path, mode) as f:
        f.write(text)
    