# DEVELOPMENT_SETUP.md

# Real Estate Lead Bot — Development Setup (MySQL)

## Core stack

```text
Frontend   → React (Vite) — run with npm later / for now optional
Backend    → Python + FastAPI
Database   → MySQL (local on your PC)
Automation → n8n (Docker or local)
AI         → LLM via n8n / provider
```

## Recommended local development

1. **MySQL on your PC** (already installed)
2. **Backend** run with Python virtualenv + uvicorn
3. **n8n** via Docker or its own install
4. **Frontend** with `npm run dev` when you need the UI

Docker is available for MySQL/n8n/backend if you want, but for day-to-day development the local MySQL + host-run backend is the simplest path.

---

## 1. MySQL database

```sql
CREATE DATABASE real_estate_leads
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
```

## 2. Environment

```bash
cp .env.example .env
```

Edit `.env`:

```env
DATABASE_URL=mysql+pymysql://root:YOUR_MYSQL_PASSWORD@localhost:3306/real_estate_leads
N8N_WEBHOOK_URL=http://localhost:5678/webhook
CORS_ORIGINS=http://localhost:5173,http://localhost:3000
```

## 3. Backend

```bash
cd backend
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

Create tables:

```bash
python -c "
from app.db.base import Base
from app.db.session import engine
from app.models import *
Base.metadata.create_all(bind=engine)
print('Tables created')
"
```

Start API:

```bash
uvicorn app.main:app --reload --port 8000
```

Docs: http://localhost:8000/docs

## 4. n8n

```bash
docker compose up -d n8n
```

Open http://localhost:5678 (admin / admin by default in compose).

Create webhook workflow path: `lead-process-message`.

## 5. Frontend (when ready)

```bash
cd frontend
npm install
npm run dev
```

→ http://localhost:5173

---

## Architecture reminder

```text
React → FastAPI → MySQL
              ↘
               n8n → AI / Notifications / Sheets
```

MySQL is the system of record. n8n orchestrates; it does not own the data.
