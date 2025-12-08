from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.schemas.question import QuestionBase
from app.services.question_service import QuestionService

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/{question_id}")
def read_question(question_id: int, db: Session = Depends(get_db)):
    result = QuestionService.get_question(db, question_id)
    if not result:
        raise HTTPException(status_code=404, detail="Question not found")
    return result


@router.post("/")
def create_question(question: QuestionBase, db: Session = Depends(get_db)):
    return QuestionService.create_question(db, question)


@router.delete("/{question_id}")
def delete_question(question_id: int, db: Session = Depends(get_db)):
    ok = QuestionService.delete_question(db, question_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Question not found")
    return {"detail": "Question deleted successfully"}
