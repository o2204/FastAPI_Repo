from fastapi import FastAPI
from app.core.database import Base, engine
from app.controllers.question_controller import router as question_router

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(question_router, prefix="/questions", tags=["Questions"])
