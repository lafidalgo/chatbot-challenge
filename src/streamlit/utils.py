import os
import json

import streamlit as st

from PIL import Image

import requests
from requests.models import Response

import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader

import config


def init_page_configuration(add_logo: bool = True):
    # Page configuration
    favicon = Image.open("src/streamlit/assets/favicon-hotmart.png")
    st.set_page_config(
        page_title="Hotmart Challenge",
        page_icon=favicon,
    )

    # Logo
    if add_logo:
        logo = Image.open("src/streamlit/assets/logo-hotmart.png")
        st.image(logo)


def import_authentication_config():
    config_path = os.environ.get(
        'STREAMLIT_AUTHENTICATOR_CONFIG_PATH', 'src/streamlit/authenticator/config.yaml')
    with open(config_path) as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['pre-authorized']
    )

    return authenticator, config


def update_authentication_config(auth_config):
    config_path = os.environ.get(
        'STREAMLIT_AUTHENTICATOR_CONFIG_PATH', 'src/streamlit/authenticator/config.yaml')
    with open(config_path, 'w') as file:
        yaml.dump(auth_config, file, default_flow_style=False)


def process_streaming_api_response(response: Response):
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Process the response stream incrementally
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                # Decode the chunk if necessary (assuming the response is in JSON format)
                data = json.loads(chunk)
                # Yield the decoded chunk
                yield data
    else:
        # Yield an error message if the request was not successful
        yield f"Error: {response.status_code}"


def process_non_streaming_api_response(response: Response):
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract data from the response
        data = response.json()
        return data
    else:
        return f"Error: {response.status_code}"


def process_api_response(response: Response, stream: bool = False):
    if stream:
        processed_response = process_streaming_api_response(response)
    else:
        processed_response = process_non_streaming_api_response(response)

    return processed_response


def send_get_api_request(url: str, params_data: dict = None, stream: bool = False):
    # Make a request to the API
    response = requests.get(url, params=params_data, stream=stream)

    return process_api_response(response, stream=stream)


def send_post_api_request(url: str, params_data: dict = None, files: dict = None, stream: bool = False):
    # Make a request to the API
    response = requests.post(url, params=params_data,
                             files=files, stream=stream)

    return process_api_response(response, stream=stream)


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


def check_openai_key_api():
    response = send_get_api_request(config.API_URLS['CHECK_OPENAI_KEY'])

    # Extract the response text from the response stream
    response_text = response["results"]

    return response_text


def check_api_status():
    api_status = send_get_api_request(config.API_URLS['GET_API_STATUS'])

    return api_status


def send_question_to_html_querying_api(collection_name: str, question: str, similarity_top_k: int = 4):
    params_data = {"collection_name": collection_name,
                   "question": question,
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


def get_available_llms():
    response = send_get_api_request(config.API_URLS['GET_AVAILABLE_LLMS'])

    llms_infos = response["results"]

    return llms_infos
