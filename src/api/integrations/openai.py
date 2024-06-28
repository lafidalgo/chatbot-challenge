import os

from openai import OpenAI


def get_openai_completions(user_prompt: str, system_prompt: str = None):
    client = OpenAI()

    model = os.environ.get("OPENAI_LLM_MODEL")

    messages = []

    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": user_prompt})

    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )

    for chunk in completion:
        completion_text = chunk.choices[0].delta.content
        if completion_text:  # Check if the text is not empty or None
            yield completion_text
