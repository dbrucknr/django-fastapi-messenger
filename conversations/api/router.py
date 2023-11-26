from fastapi import APIRouter

conversations_api = APIRouter(prefix="/conversations")

@conversations_api.get(path="")
async def conversations():
    return []

@conversations_api.get(path="/{conversation_id}")
async def detail():
    """Fetch Messages"""
    return {}

@conversations_api.post(path="/new")
async def create():
    return {}
