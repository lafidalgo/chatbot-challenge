import requests
from requests.models import Response


def process_api_response(response: Response):
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract data from the response
        data = response.json()
        return data
    else:
        return f"Error: {response.status_code}"


def send_get_api_request(url: str, params_data: dict = None):
    # Make a request to the API
    response = requests.get(url, params=params_data)

    return process_api_response(response)


def send_post_api_request(url: str, params_data: dict = None, files=None):
    # Make a request to the API
    response = requests.post(url, params=params_data, files=files)

    return process_api_response(response)
