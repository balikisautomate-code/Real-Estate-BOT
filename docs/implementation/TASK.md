# TASK.md

# PrimeHomes Realty — Real Estate Lead Bot
## Project Task Tracker

**Overall Status:** 🟡 Implementation In Progress  
**Current Phase:** Backend + MySQL + n8n wiring  
**Database:** MySQL (local on developer PC)

### Status Legend
- ⬜ Not Started | 🟡 In Progress | 🟢 Completed | 🔴 Blocked

---

## Roadmap

```text
DOCUMENTATION          🟢
PROJECT SETUP          🟢
DATABASE (MySQL)       🟢 models ready
BACKEND API            🟢 core
FRONTEND               🟢 chat + dashboard shell
N8N AUTOMATION         🟡 (you are testing)
AI PROCESSING
LEAD QUALIFICATION     🟢
TESTING
DEPLOYMENT
```

---

## Database

- [x] Switch from PostgreSQL → **MySQL**
- [x] Models use CHAR(36) UUIDs + JSON (MySQL-compatible)
- [x] PyMySQL driver
- [x] `.env.example` points to MySQL
- [x] docker-compose updated (optional MySQL service on port 3307)
- [ ] Create DB + tables on your machine
- [ ] Alembic migrations (later)

---

## Backend

- [x] Health, Leads, Conversations, Messages APIs
- [x] Qualification service
- [x] n8n webhook trigger
- [ ] Auth / JWT (next if needed)

---

## Frontend

- [x] Orange/yellow modern UI
- [x] Customer chat
- [x] Dashboard shell
- [ ] Full lead detail / follow-ups (later)

---

## Current priority (your machine)

1. Create MySQL database `real_estate_leads`
2. Set `DATABASE_URL` in `.env`
3. Install backend deps + create tables
4. Run `uvicorn`
5. Point n8n webhook to the message-processing workflow
6. Test chat → API → n8n flow
