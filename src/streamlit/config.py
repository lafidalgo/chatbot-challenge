import os
from urllib.parse import urljoin

# Get the USE_LOCAL_API environment variable and convert it to a boolean
USE_LOCAL_APIS = os.environ.get(
    'USE_LOCAL_APIS', '').lower() in ('true', '1', 't')

# Get the LOCAL_DOCUMENT_QUERYING_API_URL environment variable
local_document_querying_api_url = os.environ.get(
    'LOCAL_DOCUMENT_QUERYING_API_URL', 'http://document-querying-hotmart-challenge:8000/')

# Get the LOCAL_DOCUMENT_EXTRACTION_API_URL environment variable
local_document_extraction_api_url = os.environ.get(
    'LOCAL_DOCUMENT_EXTRACTION_API_URL', 'http://document-extraction-hotmart-challenge:8000/')

if USE_LOCAL_APIS:
    DOCUMENT_QUERYING_API_URL = local_document_querying_api_url
    DOCUMENT_EXTRACTION_API_URL = local_document_extraction_api_url
else:
    DOCUMENT_QUERYING_API_URL = os.environ.get(
        'DOCUMENT_QUERYING_API_URL', local_document_querying_api_url)
    DOCUMENT_EXTRACTION_API_URL = os.environ.get(
        'DOCUMENT_EXTRACTION_API_URL', local_document_extraction_api_url)

document_querying_endpoints = {
    'GET_API_STATUS': 'api-status/',
    'GET_ALL_QDRANT_COLLECTIONS': 'qdrant/get-all-collections/',
    'GET_OPENAI_COMPLETION': 'openai/openai-completion/',
    'CHECK_OPENAI_KEY': 'openai/check-openai/',
    'HTML_QUERYING': 'llamaindex/html-querying/',
    'GET_AVAILABLE_LLMS': 'llamaindex/get-available-llms/',
}

document_extraction_endpoints = {
    'GET_API_STATUS': 'api-status/',
    'HTML_EXTRACTION': 'llamaindex/html-extraction/',
    'FILE_EXTRACTION': 'llamaindex/file-extraction/',
}

DOCUMENT_QUERYING_API_URLS = {}
for key, endpoint in document_querying_endpoints.items():
    DOCUMENT_QUERYING_API_URLS[key] = urljoin(
        DOCUMENT_QUERYING_API_URL, endpoint)

DOCUMENT_EXTRACTION_API_URLS = {}
for key, endpoint in document_extraction_endpoints.items():
    DOCUMENT_EXTRACTION_API_URLS[key] = urljoin(
        DOCUMENT_EXTRACTION_API_URL, endpoint)
