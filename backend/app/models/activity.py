import uuid
from datetime import datetime
from sqlalchemy import String, Text, DateTime, ForeignKey, CHAR, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base


def generate_uuid() -> str:
    return str(uuid.uuid4())


class Activity(Base):
    __tablename__ = "activities"

    id: Mapped[str] = mapped_column(CHAR(36), primary_key=True, default=generate_uuid)
    lead_id: Mapped[str] = mapped_column(CHAR(36), ForeignKey("leads.id"), nullable=False)
    actor_type: Mapped[str] = mapped_column(String(50), default="SYSTEM")  # SYSTEM | AI | AGENT
    activity_type: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    metadata_: Mapped[dict | None] = mapped_column("metadata", JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    lead = relationship("Lead", back_populates="activities")
