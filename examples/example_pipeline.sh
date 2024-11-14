#!/bin/bash

# Check Document Querying API Status
echo "Checking Document Querying API Status"
curl -X GET http://localhost:8001/api-status/
echo -e "\n" # New Line

# Check Document Extraction API Status
echo "Checking Document Extraction API Status"
curl -X GET http://localhost:8000/api-status/
echo -e "\n\n" # New Line

# Send URL for HTML Extraction
echo "Sending URL for HTML Extraction"
curl -X POST 'http://localhost:8000/llamaindex/html-extraction/?collection_name=llama_3_2&html_url=https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/'
echo -e "\n\n" # New Line

# Send File for Extraction
echo "Sending File for Extraction"
curl -X POST 'http://localhost:8000/llamaindex/file-extraction/?collection_name=sample_text' -F 'file=@data/sample.txt'
echo -e "\n\n" # New Line

# Get All Qdrant Collections
echo "Getting All Qdrant Collections"
curl -X GET http://localhost:8001/qdrant/get-all-collections/
echo -e "\n\n" # New Line

# Get Available LLMS
echo "Getting Available LLMS"
curl -X GET http://localhost:8001/llamaindex/get-available-llms/
echo -e "\n\n" # New Line

# Send Question for HTML Querying
echo "Sending Question for HTML Querying"
curl -X POST "http://localhost:8001/llamaindex/html-querying/?collection_name=llama_3_2&question=What%20are%20the%20sizes%20of%20Llama%203.2%20models%3F&llm_model_name=GPT-4o%20Mini"

