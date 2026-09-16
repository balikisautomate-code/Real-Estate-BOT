"""
PrimeHomes Realty — Real Estate Lead Bot
FastAPI application entry point.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import health, leads, conversations
from app.core.config import settings

app = FastAPI(
    title="Real Estate Lead Bot API",
    description="AI-powered lead management and qualification system for PrimeHomes Realty",
    version="0.1.0",
)

origins = [o.strip() for o in settings.cors_origins.split(",") if o.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/api/v1", tags=["health"])
app.include_router(leads.router, prefix="/api/v1")
app.include_router(conversations.router, prefix="/api/v1")


@app.get("/")
def root():
    return {
        "service": "Real Estate Lead Bot API",
        "status": "running",
        "docs": "/docs",
        "version": "0.1.0",
    }
