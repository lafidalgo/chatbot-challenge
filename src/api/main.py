from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse

from pydantic import BaseModel

import src.api.integrations.qdrant as qdrant

app = FastAPI()


class CollectionInfosParams(BaseModel):
    collection_name: str


@app.get("/", tags=["API Status"])
def home():
    return RedirectResponse(url="/help/")


@app.get("/help/", tags=["API Status"])
def help():
    return """
    Hotmart Challenge
    
    /help - help endpoint
    """


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


@app.get("/test-name/")
def test_name():
    return "Test"


if __name__ == "__main__":
    import uvicorn
    # Start FastAPI
    uvicorn.run(app, port=8000, host="0.0.0.0")
