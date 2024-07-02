from urllib.parse import urljoin

DOCUMENT_QUERYING_API_URL = 'http://localhost:8001/'
DOCUMENT_EXTRACTION_API_URL = 'http://localhost:8000/'

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
