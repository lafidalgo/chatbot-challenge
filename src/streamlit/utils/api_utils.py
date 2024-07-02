import json
import requests
from requests.models import Response


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


def send_post_api_request(url: str, params_data: dict = None, files=None, stream: bool = False):
    # Make a request to the API
    response = requests.post(url, params=params_data,
                             files=files, stream=stream)

    return process_api_response(response, stream=stream)
