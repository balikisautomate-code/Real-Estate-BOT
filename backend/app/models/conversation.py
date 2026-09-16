import uuid
from datetime import datetime
from sqlalchemy import String, DateTime, ForeignKey, CHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base


def generate_uuid() -> str:
    return str(uuid.uuid4())


class Conversation(Base):
    __tablename__ = "conversations"

    id: Mapped[str] = mapped_column(CHAR(36), primary_key=True, default=generate_uuid)
    lead_id: Mapped[str] = mapped_column(CHAR(36), ForeignKey("leads.id"), nullable=False)
    channel: Mapped[str] = mapped_column(String(50), default="WEB")
    status: Mapped[str] = mapped_column(String(50), default="ACTIVE")
    external_conversation_id: Mapped[str | None] = mapped_column(String(255), nullable=True)

    started_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    ended_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    lead = relationship("Lead", back_populates="conversations")
    messages = relationship("Message", back_populates="conversation", cascade="all, delete-orphan", order_by="Message.created_at")
