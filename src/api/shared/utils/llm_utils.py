import json

import src.api.shared.integrations.openai as openai
import src.api.shared.integrations.replicate as replicate

LLMS_MODELS_INFOS_PATH = 'src/api/shared/models/llm.json'


def get_available_llms():
    with open(LLMS_MODELS_INFOS_PATH, 'r') as file:
        llm_models_infos = json.load(file)

    # Filter out the llm models that are not available
    check_openai_key = openai.check_openai_key()
    check_replicate_key = replicate.check_replicate_key()

    # Filtering the dictionary
    filtered_llm_models_infos = {}

    for model_name, model_info in llm_models_infos.items():
        provider = model_info["provider"]

        if (check_openai_key and provider == "openai") or (check_replicate_key and provider == "replicate"):
            filtered_llm_models_infos[model_name] = model_info

    return filtered_llm_models_infos
