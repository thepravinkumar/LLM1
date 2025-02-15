import openai
import os

API_KEY = os.getenv("OPENAI_API_KEY")

def query_llm(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        api_key=API_KEY
    )
    return response["choices"][0]["message"]["content"]
