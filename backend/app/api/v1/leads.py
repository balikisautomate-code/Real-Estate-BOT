from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.lead import Lead
from app.models.lead_score import LeadScore
from app.models.activity import Activity
from app.schemas.lead import LeadCreate, LeadUpdate, LeadOut, LeadListResponse
from app.services.qualification import calculate_lead_score

router = APIRouter(prefix="/leads", tags=["leads"])


@router.post("", response_model=LeadOut, status_code=201)
def create_lead(payload: LeadCreate, db: Session = Depends(get_db)):
    lead = Lead(**payload.model_dump(exclude_unset=True))
    db.add(lead)
    db.flush()

    result = calculate_lead_score(payload.model_dump())
    lead.score = result.score
    lead.classification = result.classification
    lead.status = "QUALIFYING" if result.score < 60 else "QUALIFIED"

    score_record = LeadScore(
        lead_id=lead.id,
        score=result.score,
        classification=result.classification,
        reason=result.reason,
    )
    db.add(score_record)

    activity = Activity(
        lead_id=lead.id,
        actor_type="SYSTEM",
        activity_type="LEAD_CREATED",
        description=f"Lead created. Score: {result.score} ({result.classification})",
    )
    db.add(activity)

    db.commit()
    db.refresh(lead)
    return lead


@router.get("", response_model=LeadListResponse)
def list_leads(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    status: str | None = None,
    classification: str | None = None,
    db: Session = Depends(get_db),
):
    query = db.query(Lead)
    if status:
        query = query.filter(Lead.status == status)
    if classification:
        query = query.filter(Lead.classification == classification)

    total = query.count()
    items = (
        query.order_by(Lead.created_at.desc())
        .offset((page - 1) * limit)
        .limit(limit)
        .all()
    )
    return LeadListResponse(items=items, page=page, limit=limit, total=total)


@router.get("/{lead_id}", response_model=LeadOut)
def get_lead(lead_id: str, db: Session = Depends(get_db)):
    lead = db.query(Lead).filter(Lead.id == lead_id).first()
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    return lead


@router.patch("/{lead_id}", response_model=LeadOut)
def update_lead(lead_id: str, payload: LeadUpdate, db: Session = Depends(get_db)):
    lead = db.query(Lead).filter(Lead.id == lead_id).first()
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")

    data = payload.model_dump(exclude_unset=True)
    for key, value in data.items():
        setattr(lead, key, value)

    db.commit()
    db.refresh(lead)
    return lead


@router.post("/{lead_id}/qualify", response_model=LeadOut)
def qualify_lead(lead_id: str, db: Session = Depends(get_db)):
    lead = db.query(Lead).filter(Lead.id == lead_id).first()
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")

    data = {
        "intent": lead.intent,
        "transaction_type": lead.transaction_type,
        "property_type": lead.property_type,
        "bedrooms": lead.bedrooms,
        "location": lead.location,
        "budget_min": float(lead.budget_min) if lead.budget_min else None,
        "budget_max": float(lead.budget_max) if lead.budget_max else None,
        "timeline": lead.timeline,
        "name": lead.name,
        "email": lead.email,
        "phone": lead.phone,
    }
    result = calculate_lead_score(data)

    lead.score = result.score
    lead.classification = result.classification
    if result.score >= 60:
        lead.status = "QUALIFIED"

    score_record = LeadScore(
        lead_id=lead.id,
        score=result.score,
        classification=result.classification,
        reason=result.reason,
    )
    db.add(score_record)

    activity = Activity(
        lead_id=lead.id,
        actor_type="SYSTEM",
        activity_type="SCORE_CHANGED",
        description=f"Lead re-qualified. Score: {result.score} ({result.classification}). {result.reason}",
    )
    db.add(activity)

    db.commit()
    db.refresh(lead)
    return lead
