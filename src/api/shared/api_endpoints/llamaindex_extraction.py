from fastapi import APIRouter, Depends

from pydantic import BaseModel

import src.api.shared.integrations.qdrant as qdrant

import src.api.shared.utils as utils


class HTMLExtractionParams(BaseModel):
    collection_name: str
    html_url: str


router = APIRouter()


@router.post("/html-extraction/")
async def html_extraction(params: HTMLExtractionParams = Depends()):
    results = {}

    collection_name = params.collection_name

    # Check if the collection already exists
    if qdrant.check_collection_exists(collection_name):
        return {"results": results, "params": params,
                "error": "Collection already exists."}

    # Check if the url is valid
    if not utils.is_valid_url(params.html_url):
        return {"results": results, "params": params,
                "error": "Invalid 'html_url' parameter."}

    # Build the vector store index from the uploaded files
    documents = utils.build_vector_store_index_from_url(
        collection_name, params.html_url)

    # Extract the text from the documents
    documents_text = '\n'.join(
        [document.text for document in documents])
    print("Extracted documents text:")
    print(documents_text)

    # Return the results
    results["documents"] = documents
    results["documents_text"] = documents_text

    return {"results": results, "params": params, "error": ""}
