import uuid
from datetime import datetime
from sqlalchemy import String, Integer, Numeric, DateTime, Text, CHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
import enum


class TransactionType(str, enum.Enum):
    BUY = "BUY"
    RENT = "RENT"
    SELL = "SELL"
    INQUIRE = "INQUIRE"
    UNKNOWN = "UNKNOWN"


class PropertyType(str, enum.Enum):
    APARTMENT = "APARTMENT"
    HOUSE = "HOUSE"
    DUPLEX = "DUPLEX"
    TERRACE = "TERRACE"
    DETACHED_HOUSE = "DETACHED_HOUSE"
    LAND = "LAND"
    COMMERCIAL = "COMMERCIAL"
    OFFICE = "OFFICE"
    OTHER = "OTHER"
    UNKNOWN = "UNKNOWN"


class Timeline(str, enum.Enum):
    IMMEDIATE = "IMMEDIATE"
    WITHIN_1_MONTH = "WITHIN_1_MONTH"
    WITHIN_3_MONTHS = "WITHIN_3_MONTHS"
    WITHIN_6_MONTHS = "WITHIN_6_MONTHS"
    RESEARCHING = "RESEARCHING"
    UNKNOWN = "UNKNOWN"


class LeadStatus(str, enum.Enum):
    NEW = "NEW"
    QUALIFYING = "QUALIFYING"
    QUALIFIED = "QUALIFIED"
    ASSIGNED = "ASSIGNED"
    CONTACTED = "CONTACTED"
    ENGAGED = "ENGAGED"
    VIEWING_SCHEDULED = "VIEWING_SCHEDULED"
    NEGOTIATING = "NEGOTIATING"
    NURTURE = "NURTURE"
    CONVERTED = "CONVERTED"
    LOST = "LOST"


class Classification(str, enum.Enum):
    HOT = "HOT"
    WARM = "WARM"
    COLD = "COLD"
    UNQUALIFIED = "UNQUALIFIED"


def generate_uuid() -> str:
    return str(uuid.uuid4())


class Lead(Base):
    __tablename__ = "leads"

    id: Mapped[str] = mapped_column(CHAR(36), primary_key=True, default=generate_uuid)
    name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    email: Mapped[str | None] = mapped_column(String(255), nullable=True)
    phone: Mapped[str | None] = mapped_column(String(50), nullable=True)

    property_type: Mapped[str | None] = mapped_column(String(50), nullable=True)
    transaction_type: Mapped[str | None] = mapped_column(String(50), nullable=True)
    bedrooms: Mapped[int | None] = mapped_column(Integer, nullable=True)
    bathrooms: Mapped[int | None] = mapped_column(Integer, nullable=True)
    location: Mapped[str | None] = mapped_column(String(255), nullable=True)
    budget_min: Mapped[float | None] = mapped_column(Numeric(15, 2), nullable=True)
    budget_max: Mapped[float | None] = mapped_column(Numeric(15, 2), nullable=True)
    currency: Mapped[str | None] = mapped_column(String(10), nullable=True, default="NGN")
    timeline: Mapped[str | None] = mapped_column(String(50), nullable=True)
    intent: Mapped[str | None] = mapped_column(String(50), nullable=True)

    status: Mapped[str] = mapped_column(String(50), default=LeadStatus.NEW.value)
    classification: Mapped[str | None] = mapped_column(String(50), nullable=True)
    score: Mapped[int | None] = mapped_column(Integer, nullable=True)

    source: Mapped[str | None] = mapped_column(String(100), nullable=True, default="WEBSITE")
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_contacted_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    next_follow_up_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    conversations = relationship("Conversation", back_populates="lead", cascade="all, delete-orphan")
    scores = relationship("LeadScore", back_populates="lead", cascade="all, delete-orphan")
    activities = relationship("Activity", back_populates="lead", cascade="all, delete-orphan")
