from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse, StreamingResponse

from pydantic import BaseModel
from typing import Optional

import src.api.integrations.qdrant as qdrant
import src.api.integrations.openai as openai

import src.api.utils as utils


class CollectionInfosParams(BaseModel):
    collection_name: str


class OpenAICompletionParams(BaseModel):
    user_prompt: str
    system_prompt: Optional[str] = None
    stream_response: Optional[bool] = False


class HTMLExtractionParams(BaseModel):
    collection_name: str
    html_url: str


class HTMLQueryingParams(BaseModel):
    collection_name: str
    question: str
    similarity_top_k: Optional[int] = 4


app = FastAPI()

openai.configure_llamaindex_openai_embedding()
openai.configure_llamaindex_openai_llm()
qdrant.configure_documents_chunks(chunk_size=256, chunk_overlap=30)


@app.get("/", tags=["API Status"])
def home():
    return RedirectResponse(url="/help/")


@app.get("/help/", tags=["API Status"])
def help():
    return """
    Hotmart Challenge
    
    /help - help endpoint
    """


@app.get("/api-status/", tags=["API Status"])
def api_status():
    return True


@app.get("/get-all-collections/", tags=["Qdrant Integration"])
def all_collections():
    return {"results": {"collections": qdrant.get_all_collections()},
            "params": "",
            "error": ""}


@app.get("/get-infos-collection/", tags=["Qdrant Integration"])
def infos_collection(params: CollectionInfosParams = Depends()):
    return {"results": qdrant.get_infos_collection(params.collection_name),
            "params": params,
            "error": ""}


@app.get("/collection-exists/", tags=["Qdrant Integration"])
def collection_exists(params: CollectionInfosParams = Depends()):
    return {"results": qdrant.check_collection_exists(params.collection_name),
            "params": params,
            "error": ""}


@app.get("/check-openai/", tags=["OpenAI Integration"])
def check_openai():
    return {"results": openai.check_openai_key(),
            "params": "",
            "error": ""}


@app.post("/openai-completion/", tags=["OpenAI Integration"])
async def openai_completion(params: OpenAICompletionParams = Depends()):
    stream_response = params.stream_response

    response = openai.get_openai_completions(
        params.user_prompt, params.system_prompt, stream=stream_response)

    if stream_response:
        return StreamingResponse(response, media_type='text/event-stream')
    else:
        return {"results": response,
                "params": params,
                "error": ""}


@app.post("/html-extraction/")
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


@app.post("/html-querying/")
async def html_querying(params: HTMLQueryingParams = Depends()):
    results = {}

    print("Params:", params.model_dump())

    collection_name = params.collection_name

    # Check if the collection doesn't exist
    if not qdrant.check_collection_exists(collection_name):
        return {"results": results, "params": params,
                "error": "Collection doesn't exist yet."}

    # Get the query engine from vector store
    query_engine = utils.get_query_engine_from_vector_store(
        collection_name, params.similarity_top_k)

    question = params.question

    print("Query question:", question)
    response = query_engine.query(question)
    print("Query response:", response)

    # Return the results
    results["response"] = response

    return {"results": results, "params": params, "error": ""}

if __name__ == "__main__":
    import uvicorn
    # Start FastAPI
    uvicorn.run(app, port=8000, host="0.0.0.0")
