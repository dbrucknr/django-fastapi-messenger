from django.db import models
from typing import List
from datetime import datetime
from pydantic import ConfigDict, BaseModel as _BaseModel

class BaseModel(_BaseModel):
    @classmethod
    def from_orms(cls, instances: List[models.Model]):
        return [cls.model_validate(inst) for inst in instances]


class ConversationSchema(BaseModel):
    id: int
    created_at: datetime

class MessageSchema(BaseModel):
    id: int
    sender_id: int
    conversation_id: int
    content: str
    timpestamp: datetime

    model_config = ConfigDict(from_attributes=True)

class MessageResponse(BaseModel):
    items: List[MessageSchema]

    @classmethod
    def from_qs(cls, qs):
        return cls(items=MessageSchema.from_orms(qs))
