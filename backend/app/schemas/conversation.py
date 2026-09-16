from datetime import datetime
from pydantic import BaseModel, ConfigDict
from typing import Optional


class ConversationCreate(BaseModel):
    lead_id: Optional[str] = None
    channel: str = "WEB"


class ConversationOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    lead_id: str
    channel: str
    status: str
    started_at: datetime
    created_at: datetime
