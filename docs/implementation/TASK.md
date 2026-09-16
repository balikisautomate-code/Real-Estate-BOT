# TASK.md

# PrimeHomes Realty — Real Estate Lead Bot
## Project Task Tracker

> **Purpose:** Track all development tasks required to build, test, and deploy the Real Estate Lead Bot.

---

## 1. Project Status

**Overall Status:** 🟡 Implementation In Progress  
**Current Phase:** Backend + Frontend MVP (MySQL)  
**MVP Status:** Core code written — configured for local MySQL

### Status Legend

- ⬜ Not Started
- 🟡 In Progress
- 🟢 Completed
- 🔴 Blocked
- ⏸️ On Hold

---

# 2. Development Roadmap

```text
DOCUMENTATION          🟢
     ↓
PROJECT SETUP          🟢
     ↓
DATABASE (MySQL)       🟢
     ↓
BACKEND API            🟢 (core)
     ↓
FRONTEND               🟢 (chat + dashboard shell)
     ↓
N8N AUTOMATION         🟡
     ↓
AI PROCESSING
     ↓
LEAD QUALIFICATION     🟢
     ↓
SALES DASHBOARD        🟡
     ↓
TESTING
     ↓
VPS DEPLOYMENT (Docker later)
     ↓
MVP COMPLETE
```

---

# Database

- [x] Switched to **MySQL** for local development
- [x] Models adapted (CHAR(36) UUIDs, JSON)
- [x] PyMySQL driver
- [ ] Alembic migrations (optional for now)

---

# Backend

- [x] FastAPI + CORS
- [x] Health endpoint
- [x] Lead / Conversation / Message APIs
- [x] Qualification service
- [x] n8n webhook trigger

---

# Frontend

- [x] Vite + React + TypeScript
- [x] Orange / yellow modern UI
- [x] Customer chat
- [x] Sales dashboard shell

---

# Current Priority (you on device)

1. Create MySQL database `real_estate_leads`
2. Set `DATABASE_URL` in `.env`
3. Install backend deps + create tables
4. Run backend + frontend
5. Wire n8n webhook and test

---

*Living task tracker — keep updated as work progresses.*
