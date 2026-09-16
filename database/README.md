# Database

PostgreSQL is the **system of record** for the Real Estate Lead Bot.

## Planned Tables

- `users`
- `roles`
- `leads`
- `conversations`
- `messages`
- `lead_scores`
- `lead_assignments`
- `follow_ups`
- `activities`
- `integration_syncs`

## Approach

1. SQLAlchemy models live in `backend/app/models/`
2. Alembic migrations live in `backend/alembic/`
3. Seed scripts and any pure SQL can live in this `database/` folder if needed

## Local Development

The easiest way to run PostgreSQL is via the root `docker-compose.yml`:

```bash
docker compose up -d postgres
```

Connection string (from `.env.example`):

```text
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/real_estate_leads
```
