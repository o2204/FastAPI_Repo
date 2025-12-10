from sqlalchemy.orm import Session
from app.repositories.question_repository import QuestionRepository
from app.schemas.question import QuestionBase

class QuestionService:
    def __init__(self, question_repository: QuestionRepository):
        self.question_repository = question_repository

    def get_question(self, question_id: int):
        return self.question_repository.get_question(question_id)

    def create_question(self, question: QuestionBase):
        return self.question_repository.create_question(question)

    def delete_question(self, question_id: int):
        return self.question_repository.delete_question(question_id)
