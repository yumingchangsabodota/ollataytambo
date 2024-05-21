
import requests
import json

from modules.ollama.config.ollama_config import OllamaConfig

from fastapi import APIRouter

router = APIRouter()

ollama_config = OllamaConfig()


@router.post("/summarize", tags=["Ollama AI"], summary="Given a text, Ollama AI will return a summary of the text.")
async def summarize(some_text: str):
    host = ollama_config.host
    port = ollama_config.port
    model = ollama_config.chat_model
    endpoint = f"http://{host}:{port}/api/generate"
    body = {
        "model": model,
        "options": {
            "temperature": 0.0,
            "num_predict": 200,
            "seed": 666
        },
        "prompt": f"""Base on the text below, provide a brief summary of the text:
        {some_text}""",
        "stream": False
    }
    response = requests.post(endpoint, json=body)
    return response.json()


@router.post("/embedding", tags=["Ollama AI"], summary="Given a text, Ollama AI will return the embedding vectors of the text.")
async def summarize(some_text: str):
    pass
