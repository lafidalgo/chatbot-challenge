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
curl -X POST 'http://localhost:8000/llamaindex/html-extraction/?collection_name=como_funciona_hotmart&html_url=https://hotmart.com/pt-br/blog/como-funciona-hotmart'
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
curl -X POST "http://localhost:8001/llamaindex/html-querying/?collection_name=como_funciona_hotmart&question=Onde%20fica%20a%20sede%20global%20da%20Hotmart&llm_model_name=GPT-3.5%20Turbo"

