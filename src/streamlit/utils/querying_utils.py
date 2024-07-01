import config

from .api_utils import send_post_api_request, send_get_api_request


def check_api_status():
    api_status = send_get_api_request(config.API_URLS['GET_API_STATUS'])

    return api_status


def check_openai_key_api():
    response = send_get_api_request(config.API_URLS['CHECK_OPENAI_KEY'])

    # Extract the response text from the response stream
    response_text = response["results"]

    return response_text


def get_available_llms():
    response = send_get_api_request(config.API_URLS['GET_AVAILABLE_LLMS'])

    llms_infos = response["results"]

    return llms_infos


def send_question_to_openai_api(question: str, stream: bool = False):
    system_prompt = "Você se chama João. Você é um funcionário da Hotmart que está ajudando um cliente com dúvidas sobre a empresa."

    params_data = {"user_prompt": question,
                   "system_prompt": system_prompt,
                   "stream_response": stream}

    response = send_post_api_request(
        config.API_URLS['GET_OPENAI_COMPLETION'], params_data=params_data, stream=stream)

    if stream:
        # Extract the response text from the response stream
        response_text = (response_item['content']
                         for response_item in response)
    else:
        # Extract the response text from the response stream
        response_text = response["results"]["message"]["content"]

    return response_text


def send_question_to_html_querying_api(collection_name: str, question: str, llm_model_name: str, similarity_top_k: int = 4):
    params_data = {"collection_name": collection_name,
                   "question": question,
                   "llm_model_name": llm_model_name,
                   "similarity_top_k": similarity_top_k}

    response = send_post_api_request(
        config.API_URLS['HTML_QUERYING_ENDPOINT'], params_data=params_data)

    query_references = []
    for source_nodes in response["results"]["response"]["source_nodes"]:
        node = source_nodes["node"]
        query_references.append({
            "text": node["text"],
            "score": source_nodes["score"],
        })

    query_response = response["results"]["response"]["response"]
    query_references = query_references

    return query_response, query_references
