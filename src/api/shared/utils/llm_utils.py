import json

LLMS_MODELS_INFOS_PATH = 'src/api/shared/models/llm.json'


def get_available_llms():
    with open(LLMS_MODELS_INFOS_PATH, 'r') as file:
        return json.load(file)
