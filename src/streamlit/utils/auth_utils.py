import os
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth


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
