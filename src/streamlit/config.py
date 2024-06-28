import os
from urllib.parse import urljoin

# Get the USE_LOCAL_API environment variable and convert it to a boolean
USE_LOCAL_API = os.environ.get(
    'USE_LOCAL_API', '').lower() in ('true', '1', 't')

# Get the LOCAL_GENERAL_API_URL environment variable
local_general_api_url = os.environ.get(
    'LOCAL_GENERAL_API_URL', 'http://fastapi-hotmart-challenge:8000/')

if USE_LOCAL_API:
    GENERAL_API_URL = local_general_api_url
else:
    GENERAL_API_URL = os.environ.get('GENERAL_API_URL', local_general_api_url)

endpoints = {
    'GET_TEST_NAME': 'test-name/',
}

API_URLS = {}
for key, endpoint in endpoints.items():
    API_URLS[key] = urljoin(GENERAL_API_URL, endpoint)
