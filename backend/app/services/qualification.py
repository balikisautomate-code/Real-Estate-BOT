"""
Deterministic lead qualification service.
AI extracts data; this service calculates the official score.
"""

from dataclasses import dataclass


@dataclass
class QualificationResult:
    score: int
    classification: str
    reason: str
    missing_fields: list[str]


def calculate_lead_score(lead_data: dict) -> QualificationResult:
    score = 0
    reasons = []
    missing = []

    # Intent (max 20)
    intent = (lead_data.get("intent") or lead_data.get("transaction_type") or "").upper()
    if intent in ("BUY", "RENT", "SELL", "LAND"):
        score += 20
        reasons.append("Clear intent")
    elif intent in ("PROPERTY_ENQUIRY", "INQUIRE"):
        score += 10
        reasons.append("General enquiry")
    else:
        missing.append("intent")

    # Property requirement (max 15)
    prop = (lead_data.get("property_type") or "").upper()
    bedrooms = lead_data.get("bedrooms")
    if prop and prop not in ("UNKNOWN", "OTHER", ""):
        score += 10
        reasons.append("Specific property type")
        if bedrooms and bedrooms > 0:
            score += 5
            reasons.append("Bedrooms specified")
    else:
        missing.append("property_type")

    # Location (max 15)
    location = lead_data.get("location")
    if location and len(str(location).strip()) > 2:
        score += 15
        reasons.append("Specific location")
    else:
        missing.append("location")

    # Budget (max 20)
    budget_max = lead_data.get("budget_max")
    budget_min = lead_data.get("budget_min")
    if budget_max or budget_min:
        score += 20
        reasons.append("Budget provided")
    else:
        missing.append("budget")

    # Timeline (max 20)
    timeline = (lead_data.get("timeline") or "").upper()
    timeline_scores = {
        "IMMEDIATE": 20,
        "WITHIN_1_MONTH": 18,
        "WITHIN_3_MONTHS": 15,
        "WITHIN_6_MONTHS": 10,
        "RESEARCHING": 5,
    }
    if timeline in timeline_scores:
        score += timeline_scores[timeline]
        reasons.append(f"Timeline: {timeline}")
    else:
        missing.append("timeline")

    # Contact (max 10)
    if lead_data.get("phone"):
        score += 5
        reasons.append("Phone available")
    if lead_data.get("email"):
        score += 3
        reasons.append("Email available")
    if lead_data.get("name"):
        score += 2
        reasons.append("Name available")

    score = min(score, 100)

    if score >= 80:
        classification = "HOT"
    elif score >= 60:
        classification = "WARM"
    elif score >= 30:
        classification = "COLD"
    else:
        classification = "UNQUALIFIED"

    reason = "; ".join(reasons) if reasons else "Insufficient information"

    return QualificationResult(
        score=score,
        classification=classification,
        reason=reason,
        missing_fields=missing,
    )
