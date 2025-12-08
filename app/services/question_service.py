from sqlalchemy.orm import Session
from app.repositories.question_repository import QuestionRepository
from app.schemas.question import QuestionBase

class QuestionService:

    @staticmethod
    def get_question(db: Session, question_id: int):
        return QuestionRepository.get_question(db, question_id)

    @staticmethod
    def create_question(db: Session, question: QuestionBase):
        return QuestionRepository.create_question(db, question)

    @staticmethod
    def delete_question(db: Session, question_id: int):
        return QuestionRepository.delete_question(db, question_id)
