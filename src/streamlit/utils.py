import os

import streamlit as st

from PIL import Image

import requests
from requests.models import Response

import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader


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


def process_api_response(response: Response):
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract data from the response
        data = response.json()
        # Print the data
        print(data)
        # Return the data as needed
        return data
    else:
        # Return an error message if the request was not successful
        return f"Error: {response.status_code}"


def send_get_api_request(url: str, params_data: dict = None):
    # Make a request to the API
    response = requests.get(url, params=params_data)

    return process_api_response(response)


def send_post_api_request(url: str, params_data: dict = None, files: dict = None):
    # Make a request to the API
    response = requests.post(url, params=params_data, files=files)

    return process_api_response(response)
