import os

from llama_index.core import Settings
from llama_index.llms.replicate import Replicate


def check_replicate_key():
    return bool(os.environ.get('REPLICATE_API_TOKEN'))


def configure_llamaindex_replicate_llm(llm_model_id: str = None):
    if llm_model_id:
        model = llm_model_id
    else:
        model = os.environ.get("REPLICATE_LLM_MODEL", "meta/llama-2-7b-chat")

    if not model:
        raise ValueError(
            "Missing environment variables for REPLICATE configuration.")

    llm_model = Replicate(
        model=model,
    )
    Settings.llm = llm_model
