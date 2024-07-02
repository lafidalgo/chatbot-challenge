from fastapi import FastAPI

import src.api.shared.integrations.qdrant as qdrant
import src.api.shared.integrations.openai as openai

from src.api.shared.api_endpoints import api_status, qdrant_integration, llamaindex_extraction

app = FastAPI()

openai.configure_llamaindex_openai_embedding()
qdrant.configure_documents_chunks(chunk_size=256, chunk_overlap=30)

app.include_router(api_status.router, tags=["API Status"])
app.include_router(qdrant_integration.router,
                   prefix="/qdrant", tags=["Qdrant Integration"])
app.include_router(llamaindex_extraction.router,
                   prefix="/llamaindex", tags=["LlamaIndex Integration"])


if __name__ == "__main__":
    import uvicorn
    # Start FastAPI
    uvicorn.run(app, port=8000, host="0.0.0.0")
