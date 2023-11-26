from fastapi import APIRouter, Depends
from django.contrib.auth import get_user, get_user_model

from conversations.models import Conversation, Message

conversations_api = APIRouter(prefix="/conversations")
user_model = get_user_model()

@conversations_api.get(path="")
async def my_conversations():
    # Hard coded for now - need to establish user session / auth
    user = await user_model.objects.aget(id=1)
    conversations_participating_in = await Conversation.objects.afilter(participants=user)
    return conversations_participating_in

@conversations_api.get(path="/{conversation_id}")
async def conversation_messages(conversation_id: int):
    # TODO: Make sure the selected conversation is one where the user
    # is participating
    conversation = await Conversation.objects.aget(id=conversation_id)
    print(conversation)
    conversation_messages = await conversation.messages.aall()
    return conversation_messages

@conversations_api.post(path="/new")
async def create():
    return {}
