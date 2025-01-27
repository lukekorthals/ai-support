def create_openai_message(role: str, content: str) -> list:
    return [{"role": role, "content": content}]