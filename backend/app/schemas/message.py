from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from typing import Optional


class MessageCreate(BaseModel):
    content: str = Field(..., min_length=1)
    sender_type: str = "CUSTOMER"


class MessageOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    conversation_id: str
    sender_type: str
    content: str
    processing_status: str
    created_at: datetime


class MessageListResponse(BaseModel):
    items: list[MessageOut]
    page: int
    limit: int
    total: int
