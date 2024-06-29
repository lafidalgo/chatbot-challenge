import os
import json

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
        stream_options={"include_usage": True},
    )

    for chunk in completion:
        if chunk.choices:
            completion_text = chunk.choices[0].delta.content
            if completion_text:  # Check if the text is not empty or None
                response = {
                    "content": completion_text,
                    "model": chunk.model,
                    "usage": chunk.usage
                }
                yield json.dumps(response)


def check_openai_key():
    return bool(os.environ.get('OPENAI_API_KEY'))
