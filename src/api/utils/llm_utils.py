import json


def get_available_llms():
    with open('src/api/models/llm.json', 'r') as file:
        return json.load(file)
