import os
import io
import mimetypes

import utils.api_utils as api_utils
import utils.api_endpoints as api_endpoints

# ----------------------- DOCUMENT EXTRACTION API -----------------------


def check_document_extraction_api_status():
    try:
        api_status = api_utils.send_get_api_request(
            api_endpoints.DOCUMENT_EXTRACTION_API_URLS['GET_API_STATUS'])
    except Exception as e:
        api_status = e

    return api_status


def send_url_to_document_extraction_api(url: str, collection_name: str):
    params_data = {"collection_name": collection_name,
                   "html_url": url}

    response = api_utils.send_post_api_request(
        api_endpoints.DOCUMENT_EXTRACTION_API_URLS['HTML_EXTRACTION'], params_data=params_data)

    response_results = response["results"]

    return response_results


def send_file_to_document_extraction_api(file_path: str, collection_name: str):
    with open(file_path, 'rb') as f:
        file_content = io.BytesIO(f.read())
    filename = os.path.basename(file_path)

    params_data = {"collection_name": collection_name}

    files = {'file': (filename, file_content,
                      mimetypes.guess_type(filename)[0])}

    response = api_utils.send_post_api_request(
        api_endpoints.DOCUMENT_EXTRACTION_API_URLS['FILE_EXTRACTION'], params_data=params_data, files=files)

    response_results = response["results"]

    return response_results

# ----------------------- DOCUMENT QUERYING API -----------------------


def check_document_querying_api_status():
    try:
        api_status = api_utils.send_get_api_request(
            api_endpoints.DOCUMENT_QUERYING_API_URLS['GET_API_STATUS'])
    except Exception as e:
        api_status = e

    return api_status


def get_all_qdrant_collections():
    response = api_utils.send_get_api_request(
        api_endpoints.DOCUMENT_QUERYING_API_URLS['GET_ALL_QDRANT_COLLECTIONS'])

    collections = [collection["name"]
                   for collection in response["results"]["collections"]]

    return collections


def get_available_llms():
    response = api_utils.send_get_api_request(
        api_endpoints.DOCUMENT_QUERYING_API_URLS['GET_AVAILABLE_LLMS'])

    llms_infos = response["results"]

    llm_models_names = list(llms_infos.keys())

    return llm_models_names


def send_question_to_html_querying_api(collection_name: str, question: str, llm_model_name: str, similarity_top_k: int = 4):
    params_data = {"collection_name": collection_name,
                   "question": question,
                   "llm_model_name": llm_model_name,
                   "similarity_top_k": similarity_top_k}

    response = api_utils.send_post_api_request(
        api_endpoints.DOCUMENT_QUERYING_API_URLS['HTML_QUERYING'], params_data=params_data)

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


if __name__ == "__main__":
    # 1) Get the API URLs from the config
    print("1) Checking the API URLs...")
    print("Document Querying API URL:", api_endpoints.DOCUMENT_QUERYING_API_URL)
    print("Document Extraction API URL:",
          api_endpoints.DOCUMENT_EXTRACTION_API_URL)
    print()

    # 2) Check the status of the APIs
    print("2) Checking the status of the APIs...")
    document_querying_api_status = check_document_querying_api_status()
    print("Document Querying API Status:", document_querying_api_status)
    document_extraction_api_status = check_document_extraction_api_status()
    print("Document Extraction API Status:", document_extraction_api_status)
    print()

    # 3) Send a URL to the Document Extraction API
    url = "https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/"
    url_collection_name = "llama_3_2"
    print(f"3) Sending URL '{url}' to the Document Extraction API...")
    response_results = send_url_to_document_extraction_api(
        url, url_collection_name)
    if 'documents' in response_results:
        print("Successfully extracted the documents from the URL.")
    print()

    # 4) Send a file to the Document Extraction API
    file_path = "examples/data/sample.txt"
    sample_file_collection_name = "sample_text"
    print(f"4) Sending file '{file_path}' to the Document Extraction API...")
    response_results = send_file_to_document_extraction_api(
        file_path, sample_file_collection_name)
    if 'documents' in response_results:
        print("Successfully extracted the documents from the sample file.")
    print()

    # 5) Get all Qdrant collections
    print("5) Getting all Qdrant collections...")
    collections = get_all_qdrant_collections()
    print("Qdrant Collections:", collections)
    print()

    # 6) Get available LLMS
    print("6) Getting available LLMS...")
    llm_models_names = get_available_llms()
    print("Available LLMS:", llm_models_names)
    print()

    # 7) Send a question to the Document Querying API
    print("7) Sending a question to the Document Querying API...")
    question = "What are the sizes of Llama 3.2 models?"
    print(f"Question: {question}")
    collection_name = "llama_3_2"
    llm_model_name = "GPT-4o Mini"
    query_response, query_references = send_question_to_html_querying_api(
        collection_name, question, llm_model_name)
    print("Query Response:", query_response)
    print("Query References:")
    for index, reference in enumerate(query_references):
        print(f"Reference {index + 1}: - Score: {reference['score']}")
        print(reference['text'])
        print()
