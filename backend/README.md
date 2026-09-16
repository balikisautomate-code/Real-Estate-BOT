# Backend — FastAPI

This is the FastAPI application for the **PrimeHomes Realty Real Estate Lead Bot**.

## Responsibilities

- API endpoints
- Request validation
- Authentication & authorization
- Business rules
- Database access (via SQLAlchemy)
- Lead, conversation, and message management
- Integration boundary with n8n

## Recommended Structure

```text
backend/
├── app/
│   ├── main.py
│   ├── api/
│   │   └── v1/
│   │       ├── auth.py
│   │       ├── leads.py
│   │       ├── conversations.py
│   │       ├── messages.py
│   │       ├── followups.py
│   │       └── health.py
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── repositories/
│   ├── core/
│   └── db/
├── tests/
├── alembic/
├── requirements.txt
├── Dockerfile
└── README.md
```

## Local Development

```bash
cd backend
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

API docs will be available at: http://localhost:8000/docs
