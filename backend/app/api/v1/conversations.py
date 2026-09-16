from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.lead import Lead
from app.models.conversation import Conversation
from app.models.message import Message
from app.models.activity import Activity
from app.schemas.conversation import ConversationCreate, ConversationOut
from app.schemas.message import MessageCreate, MessageOut, MessageListResponse
from app.services.n8n import trigger_message_processing

router = APIRouter(prefix="/conversations", tags=["conversations"])


@router.post("", response_model=ConversationOut, status_code=201)
def create_conversation(payload: ConversationCreate, db: Session = Depends(get_db)):
    lead_id = payload.lead_id

    if not lead_id:
        # Create a new empty lead for this conversation
        lead = Lead(status="NEW", source="WEBSITE")
        db.add(lead)
        db.flush()
        lead_id = lead.id

        activity = Activity(
            lead_id=lead.id,
            actor_type="SYSTEM",
            activity_type="LEAD_CREATED",
            description="Lead created from new conversation",
        )
        db.add(activity)
    else:
        lead = db.query(Lead).filter(Lead.id == lead_id).first()
        if not lead:
            raise HTTPException(status_code=404, detail="Lead not found")

    conversation = Conversation(lead_id=lead_id, channel=payload.channel)
    db.add(conversation)
    db.commit()
    db.refresh(conversation)
    return conversation


@router.get("/{conversation_id}", response_model=ConversationOut)
def get_conversation(conversation_id: UUID, db: Session = Depends(get_db)):
    conversation = db.query(Conversation).filter(Conversation.id == conversation_id).first()
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return conversation


@router.get("/{conversation_id}/messages", response_model=MessageListResponse)
def list_messages(
    conversation_id: UUID,
    page: int = 1,
    limit: int = 50,
    db: Session = Depends(get_db),
):
    conversation = db.query(Conversation).filter(Conversation.id == conversation_id).first()
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")

    query = db.query(Message).filter(Message.conversation_id == conversation_id)
    total = query.count()
    items = (
        query.order_by(Message.created_at.asc())
        .offset((page - 1) * limit)
        .limit(limit)
        .all()
    )
    return MessageListResponse(items=items, page=page, limit=limit, total=total)


@router.post("/{conversation_id}/messages", response_model=MessageOut, status_code=201)
async def create_message(
    conversation_id: UUID,
    payload: MessageCreate,
    db: Session = Depends(get_db),
):
    conversation = db.query(Conversation).filter(Conversation.id == conversation_id).first()
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")

    message = Message(
        conversation_id=conversation_id,
        sender_type=payload.sender_type,
        content=payload.content,
        processing_status="RECEIVED",
    )
    db.add(message)
    db.commit()
    db.refresh(message)

    # Trigger n8n for customer messages
    if payload.sender_type == "CUSTOMER":
        message.processing_status = "PROCESSING"
        db.commit()
        await trigger_message_processing(
            message_id=str(message.id),
            conversation_id=str(conversation_id),
            lead_id=str(conversation.lead_id),
        )

    return message
