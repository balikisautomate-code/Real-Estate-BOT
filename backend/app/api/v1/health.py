"""Health check endpoint."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check():
    """Simple health endpoint to verify the API is running."""
    return {
        "status": "ok",
        "service": "real-estate-lead-bot",
        "version": "0.1.0",
    }
