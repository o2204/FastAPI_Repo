from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.question import QuestionBase
from app.services.question_service import QuestionService
from app.repositories.question_repository import QuestionRepository
from app.controllers.question_controller import QuestionController

router = APIRouter()

# Dependency Injection Setup
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_repository(db: Session = Depends(get_db)) -> QuestionRepository:
    return QuestionRepository(db)

def get_service(repo: QuestionRepository = Depends(get_repository)) -> QuestionService:
    return QuestionService(repo)

def get_controller(service: QuestionService = Depends(get_service)) -> QuestionController:
    return QuestionController(service)

# Routes
@router.get("/{question_id}")
def read_question(question_id: int, controller: QuestionController = Depends(get_controller)):
    return controller.read_question(question_id)

@router.post("/")
def create_question(question: QuestionBase, controller: QuestionController = Depends(get_controller)):
    return controller.create_question(question)

@router.delete("/{question_id}")
def delete_question(question_id: int, controller: QuestionController = Depends(get_controller)):
    return controller.delete_question(question_id)
