from fastapi import FastAPI

import src.api.shared.integrations.openai as openai

from src.api.shared.api_endpoints import api_status, qdrant_integration, openai_integration, llamaindex_querying

app = FastAPI()

openai.configure_llamaindex_openai_embedding()

app.include_router(api_status.router, tags=["API Status"])
app.include_router(qdrant_integration.router,
                   prefix="/qdrant", tags=["Qdrant Integration"])
app.include_router(openai_integration.router,
                   prefix="/openai", tags=["OpenAI Integration"])
app.include_router(llamaindex_querying.router,
                   prefix="/llamaindex", tags=["LlamaIndex Integration"])


if __name__ == "__main__":
    import uvicorn
    # Start FastAPI
    uvicorn.run(app, port=8000, host="0.0.0.0")
