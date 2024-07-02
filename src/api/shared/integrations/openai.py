import os
import json

import tiktoken
from openai import OpenAI

from llama_index.core import Settings
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding


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


def configure_llamaindex_openai_embedding():
    model = os.environ.get("OPENAI_EMBED_MODEL", "text-embedding-3-large")

    if not model:
        raise ValueError(
            "Missing environment variables for OPENAI configuration.")

    embed_model = OpenAIEmbedding(
        model=model,
    )
    Settings.embed_model = embed_model


def configure_llamaindex_openai_llm(llm_model_id: str = None):
    if llm_model_id:
        model = llm_model_id
    else:
        model = os.environ.get("OPENAI_LLM_MODEL", "gpt-3.5-turbo")

    if not model:
        raise ValueError(
            "Missing environment variables for OPENAI configuration.")

    llm_model = OpenAI(
        model=model,
    )
    Settings.llm = llm_model
    Settings.tokenizer = tiktoken.encoding_for_model(model).encode
