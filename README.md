# REAL ESTATE LEAD BOT

## PrimeHomes Realty

> An AI-powered real estate lead management system that receives customer enquiries, understands their requirements, qualifies leads, stores customer information, and helps the sales team follow up efficiently.

**Primary database: MySQL**  
**Backend: FastAPI**  
**Frontend: React**  
**Automation: n8n**

---

# Quick start (development)

### 1. MySQL (on your PC)

```sql
CREATE DATABASE real_estate_leads CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 2. Environment

```bash
cp .env.example .env
# Edit DATABASE_URL with your MySQL user/password
```

Example:

```env
DATABASE_URL=mysql+pymysql://root:your_password@localhost:3306/real_estate_leads
```

### 3. Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS/Linux
pip install -r requirements.txt

python -c "from app.db.base import Base; from app.db.session import engine; from app.models import *; Base.metadata.create_all(bind=engine); print('OK')"

uvicorn app.main:app --reload --port 8000
```

API docs → http://localhost:8000/docs

### 4. n8n (optional Docker)

```bash
docker compose up -d n8n
```

### 5. Frontend (when you need the UI)

```bash
cd frontend
npm install
npm run dev
```

→ http://localhost:5173

---

# Architecture

```text
CUSTOMER → React → FastAPI → MySQL
                        ↘
                         n8n → AI / Notifications / Sheets
```

Full documentation lives under `docs/`.
