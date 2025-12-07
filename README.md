# FastAPI Quiz Application

A simple RESTful API for a Quiz Application built with FastAPI, SQLAlchemy, and PostgreSQL.

## Features

- **Questions**: Create, read, and delete questions.
- **Choices**: Create and read choices associated with questions.
- **Database**: PostgreSQL integration for persistent data storage.
- **ORM**: SQLAlchemy for database interactions.

## Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: [PostgreSQL](https://www.postgresql.org/)
- **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/)
- **Driver**: `psycopg2-binary`

## Prerequisites

- Python 3.7+
- PostgreSQL installed and running locally.

## Installation & Setup

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Database Configuration:**
   
   > [!IMPORTANT]
   > Update the database connection URL in `database.py` with your PostgreSQL credentials.
   
   Open `database.py` and modify the `URL_DATABASE` variable:
   ```python
   # Format: postgresql://<username>:<password>@<host>:<port>/<database_name>
   URL_DATABASE = "postgresql://postgres:root@localhost:5432/QuizApplicationYT"
   ```
   Ensure you create the database `QuizApplicationYT` in PostgreSQL before running the app, or update the name in the connection string.

## Running the Application

Start the development server with `uvicorn`:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

### Questions

- `GET /questions/{question_id}` - Get a specific question.
- `POST /questions/` - Create a new question with choices.
- `DELETE /questions/{question_id}` - Delete a question.

### Choices

- `GET /choices/{question_id}` - Get all choices for a specific question.
- `POST /choices/` - Create a new choice for a question.

## Interactive Documentation

FastAPI provides automatic interactive API documentation. Once the app is running, visit:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)