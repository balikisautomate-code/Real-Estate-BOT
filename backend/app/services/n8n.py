"""
Helper to trigger n8n workflows.
"""

import httpx
from app.core.config import settings


async def trigger_message_processing(
    message_id: str,
    conversation_id: str,
    lead_id: str,
) -> dict | None:
    """
    Notify n8n that a new customer message is ready for AI processing.
    n8n should expose a webhook (e.g. PRH-LEAD-PROCESS-MESSAGE).
    """
    if not settings.n8n_webhook_url:
        return None

    url = f"{settings.n8n_webhook_url.rstrip('/')}/lead-process-message"
    payload = {
        "event": "MESSAGE_RECEIVED",
        "message_id": str(message_id),
        "conversation_id": str(conversation_id),
        "lead_id": str(lead_id),
    }

    headers = {}
    if settings.n8n_webhook_secret:
        headers["X-Webhook-Secret"] = settings.n8n_webhook_secret

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.post(url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json() if response.content else {"status": "triggered"}
    except Exception as e:
        # Do not fail the main request if n8n is temporarily unavailable
        print(f"[n8n] Failed to trigger workflow: {e}")
        return None
