import os
import json

from openai import OpenAI


def get_streaming_openai_completions(client, model: str, messages: list):
    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
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


def get_non_streaming_openai_completions(client, model: str, messages: list):
    completion = client.chat.completions.create(
        model=model,
        messages=messages,
    )

    return completion.choices[0]


def get_openai_completions(user_prompt: str, system_prompt: str = None, stream: bool = False):
    client = OpenAI()

    model = os.environ.get("OPENAI_LLM_MODEL", "gpt-3.5-turbo")

    messages = []

    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": user_prompt})

    if stream:
        return get_streaming_openai_completions(client, model, messages)
    else:
        return get_non_streaming_openai_completions(client, model, messages)


def check_openai_key():
    return bool(os.environ.get('OPENAI_API_KEY'))
