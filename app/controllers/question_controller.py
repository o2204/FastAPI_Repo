from fastapi import HTTPException
from app.schemas.question import QuestionBase
from app.services.question_service import QuestionService

class QuestionController:
    def __init__(self, service: QuestionService):
        self.service = service

    def read_question(self, question_id: int):
        result = self.service.get_question(question_id)
        if not result:
            raise HTTPException(status_code=404, detail="Question not found")
        return result

    def create_question(self, question: QuestionBase):
        return self.service.create_question(question)

    def delete_question(self, question_id: int):
        ok = self.service.delete_question(question_id)
        if not ok:
            raise HTTPException(status_code=404, detail="Question not found")
        return {"detail": "Question deleted successfully"}
