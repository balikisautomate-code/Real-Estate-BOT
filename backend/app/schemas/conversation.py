from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, ConfigDict
from typing import Optional


class ConversationCreate(BaseModel):
    lead_id: Optional[UUID] = None
    channel: str = "WEB"


class ConversationOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    lead_id: UUID
    channel: str
    status: str
    started_at: datetime
    created_at: datetime
