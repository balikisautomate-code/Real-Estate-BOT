from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class LeadBase(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    property_type: Optional[str] = None
    transaction_type: Optional[str] = None
    bedrooms: Optional[int] = None
    bathrooms: Optional[int] = None
    location: Optional[str] = None
    budget_min: Optional[float] = None
    budget_max: Optional[float] = None
    currency: Optional[str] = "NGN"
    timeline: Optional[str] = None
    intent: Optional[str] = None
    source: Optional[str] = "WEBSITE"
    notes: Optional[str] = None


class LeadCreate(LeadBase):
    pass


class LeadUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    property_type: Optional[str] = None
    transaction_type: Optional[str] = None
    bedrooms: Optional[int] = None
    bathrooms: Optional[int] = None
    location: Optional[str] = None
    budget_min: Optional[float] = None
    budget_max: Optional[float] = None
    currency: Optional[str] = None
    timeline: Optional[str] = None
    intent: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None


class LeadOut(LeadBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    status: str
    classification: Optional[str] = None
    score: Optional[int] = None
    created_at: datetime
    updated_at: datetime
    last_contacted_at: Optional[datetime] = None
    next_follow_up_at: Optional[datetime] = None


class LeadListResponse(BaseModel):
    items: list[LeadOut]
    page: int
    limit: int
    total: int
