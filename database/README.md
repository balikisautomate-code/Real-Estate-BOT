# Database

**MySQL** is the system of record for local development and the current implementation.

> Docker / containerised databases will be used later for deployment. For now we use the MySQL instance already running on your machine.

## Connection string

```text
mysql+pymysql://USER:PASSWORD@localhost:3306/real_estate_leads
```

Example in `.env`:

```env
DATABASE_URL=mysql+pymysql://root:your_password@localhost:3306/real_estate_leads
```

## Create the database (once)

In MySQL:

```sql
CREATE DATABASE real_estate_leads CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

## Tables (created by the app)

- `leads`
- `conversations`
- `messages`
- `lead_scores`
- `activities`

## Create tables from Python

```bash
cd backend
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
python -c "
from app.db.base import Base
from app.db.session import engine
from app.models import *
Base.metadata.create_all(bind=engine)
print('Tables created successfully')
"
```

## Notes

- UUIDs are stored as `CHAR(36)` for MySQL compatibility.
- JSON columns use MySQL `JSON` type.
- Alembic migrations can be added later when the schema stabilises.
