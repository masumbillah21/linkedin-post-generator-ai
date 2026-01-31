def clean_llm_output(text: str) -> str:
    """
    Removes empty or populated <think>...</think> blocks safely.
    """
    if not text:
        return text

    while "<think>" in text and "</think>" in text:
        start = text.find("<think>")
        end = text.find("</think>") + len("</think>")
        text = text[:start] + text[end:]

    return text.strip()
