"""
PrimeHomes Realty — Real Estate Lead Bot
FastAPI application entry point.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import health

app = FastAPI(
    title="Real Estate Lead Bot API",
    description="AI-powered lead management and qualification system for PrimeHomes Realty",
    version="0.1.0",
)

# CORS – adjust origins via environment in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router, prefix="/api/v1", tags=["health"])


@app.get("/")
def root():
    return {
        "service": "Real Estate Lead Bot API",
        "status": "running",
        "docs": "/docs",
    }
