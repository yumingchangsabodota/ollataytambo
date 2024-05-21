from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from modules.ollama.router import ollama_router

tags = [
    {
        'name': 'Ollama AI',
        'description': 'Ollama API'
    },
]

origins = ["*"]
app = FastAPI(title="Ollataytambo Backend API",
              openapi_tags=tags,
              version="0.1.0",
              docs_url="/api/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ollama_router.router,
                   prefix="/api/ollama", tags=["Ollama AI"])
