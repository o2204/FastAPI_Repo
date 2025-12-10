# FastAPI Quiz Application

A robust, layered RESTful API for a Quiz Application built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**.

## Architecture
This project follows a strict **5-Layer Architecture** to ensure separation of concerns and maintainability:

1.  **API Layer** (`app/api`): Handles HTTP routes and requests.
2.  **Controller Layer** (`app/controllers`): Orchestrates business logic flow.
3.  **Service Layer** (`app/services`): Contains core business logic.
4.  **Repository Layer** (`app/repositories`): Manages data access and DB transactions.
5.  **Client Layer** (`app/client`): Internal Python client/SDK for API interaction.

Dependency Injection (DI) is used throughout using FastAPI's `Depends` system.

## Tech Stack
-   **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
-   **Database**: [PostgreSQL](https://www.postgresql.org/)
-   **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/)
-   **Containerization**: Docker & Docker Compose

## Setup & configuration

### Prerequisites
-   Docker Desktop
-   Python 3.10+ (for local development)

### Environment
The application uses a `.env` file for configuration.
> **Note**: The Database is configured to run on host port **5434** to avoid conflicts with local Postgres instances.

## Running the Application

### 1. Start Database (Docker)
```bash
docker compose up -d
```
This starts the PostgreSQL container on port `5434`.

### 2. Run API Application
You can run the application locally using `uvicorn`:

```bash
uvicorn app.main:app --reload
```
The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## API & Testing

### Interactive Documentation
-   **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
-   **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Check Endpoints
-   `GET /api/questions/{id}`
-   `POST /api/questions/`
-   `DELETE /api/questions/{id}`

### using the Client SDK
An internal python client is available in `app/client/api_client.py`:
```python
from app.client.api_client import APIClient

client = APIClient(base_url="http://127.0.0.1:8000")
client.create_question(...)
```
