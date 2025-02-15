from src.llm_helper import query_llm

def summarize_text(text):
    prompt = f"Summarize this text: {text}"
    return query_llm(prompt)
