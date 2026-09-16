import uuid
from datetime import datetime
from sqlalchemy import String, Text, DateTime, ForeignKey, CHAR, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base


def generate_uuid() -> str:
    return str(uuid.uuid4())


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[str] = mapped_column(CHAR(36), primary_key=True, default=generate_uuid)
    conversation_id: Mapped[str] = mapped_column(CHAR(36), ForeignKey("conversations.id"), nullable=False)
    sender_type: Mapped[str] = mapped_column(String(50), nullable=False)  # CUSTOMER | BOT | AGENT | SYSTEM
    content: Mapped[str] = mapped_column(Text, nullable=False)
    external_message_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    processing_status: Mapped[str] = mapped_column(String(50), default="RECEIVED")  # RECEIVED | PROCESSING | PROCESSED | FAILED
    metadata_: Mapped[dict | None] = mapped_column("metadata", JSON, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    conversation = relationship("Conversation", back_populates="messages")
