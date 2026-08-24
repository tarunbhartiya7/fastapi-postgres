# Task Management API

A FastAPI app for managing tasks, backed by PostgreSQL and SQLAlchemy.

## Stack

- **FastAPI** — API framework
- **SQLAlchemy** — ORM
- **PostgreSQL** — database (via Docker Compose)
- **psycopg2** — Postgres driver

## Prerequisites

- Python 3.11+
- Docker & Docker Compose

## Setup

1. **Clone and enter the project**

```bash
cd task-mgmt
```

2. **Create a virtual environment and install dependencies**

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

3. **Configure environment**

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/postgres
```

4. **Start PostgreSQL**

```bash
docker compose up -d
```

5. **Run the API**

```bash
fastapi dev main.py
```

The app starts at [http://127.0.0.1:8000](http://127.0.0.1:8000). Interactive docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## API

| Method | Path         | Description        |
|--------|--------------|--------------------|
| GET    | `/health`    | Health check       |
| GET    | `/api/tasks` | List all tasks     |

## Project structure

```text
task-mgmt/
├── main.py                 # App entrypoint
├── docker-compose.yml      # Postgres service
├── requirements.txt
├── .env                    # Local secrets (not committed)
└── src/
    ├── tasks/
    │   └── models.py       # Task ORM model
    └── utils/
        ├── config.py       # Env loading
        └── db.py           # Engine, sessions, init_db
```

## Database

Tables are created on startup via `init_db()` (`Base.metadata.create_all`).

Stop Postgres:

```bash
docker compose down
```
