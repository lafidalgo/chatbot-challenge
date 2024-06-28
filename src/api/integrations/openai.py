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
        messages=messages
    )

    return completion.choices[0].message
