

from fastapi import APIRouter

router = APIRouter()


@router.post("/summarize", tags=["Ollama AI"], summary="Given a text, Ollama AI will return a summary of the text.")
async def summarize(some_text: str):
    pass


@router.post("/embedding", tags=["Ollama AI"], summary="Given a text, Ollama AI will return the embedding vectors of the text.")
async def summarize(some_text: str):
    pass
