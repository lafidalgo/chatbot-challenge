import io
import mimetypes

import config

from .api_utils import send_post_api_request, send_get_api_request


def check_document_extraction_api_status():
    try:
        api_status = send_get_api_request(
            config.DOCUMENT_EXTRACTION_API_URLS['GET_API_STATUS'])
    except:
        api_status = False

    return api_status


def send_url_to_document_extraction_api(url: str, collection_name: str):
    params_data = {"collection_name": collection_name,
                   "html_url": url}

    response = send_post_api_request(
        config.DOCUMENT_EXTRACTION_API_URLS['HTML_EXTRACTION'], params_data=params_data)

    response_text = response["results"]

    return response_text


def send_file_to_document_extraction_api(file: io.BytesIO, collection_name: str):
    params_data = {"collection_name": collection_name}

    files = {'file': (file.name, file, mimetypes.guess_type(file.name)[0])}

    response = send_post_api_request(
        config.DOCUMENT_EXTRACTION_API_URLS['FILE_EXTRACTION'], params_data=params_data, files=files)

    response_text = response["results"]

    return response_text
