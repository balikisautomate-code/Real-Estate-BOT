# Database — MySQL

**MySQL** is the system of record for the Real Estate Lead Bot.

## Development (recommended)

Use the **MySQL already installed on your PC**.

1. Create the database:

```sql
CREATE DATABASE real_estate_leads CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

2. Set the connection string in `.env`:

```env
DATABASE_URL=mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/real_estate_leads
```

Replace `root` / `YOUR_PASSWORD` with your real MySQL user and password.

3. Create tables from the backend folder:

```bash
cd backend
python -c "
from app.db.base import Base
from app.db.session import engine
from app.models import *
Base.metadata.create_all(bind=engine)
print('MySQL tables created successfully')
"
```

## Optional: MySQL inside Docker

If you prefer not to use the MySQL on your PC:

```bash
docker compose up -d mysql
```

Then point `.env` to:

```env
DATABASE_URL=mysql+pymysql://realestate:realestate@localhost:3307/real_estate_leads
```

(Port **3307** is mapped so it does not conflict with your local MySQL on 3306.)

## Core tables

- `leads`
- `conversations`
- `messages`
- `lead_scores`
- `activities`

(IDs are stored as `CHAR(36)` UUIDs for MySQL compatibility.)

## Notes

- Driver: **PyMySQL** (`mysql+pymysql://...`)
- Character set: `utf8mb4`
- PostgreSQL is no longer used in this project.
