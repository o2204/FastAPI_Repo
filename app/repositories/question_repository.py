from sqlalchemy.orm import Session
from app.models.question import Questions, Choices
from app.schemas.question import QuestionBase, ChoiceBase

class QuestionRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_question(self, question_id: int):
        return self.db.query(Questions).filter(Questions.id == question_id).first()

    def create_question(self, question: QuestionBase):
        db_question = Questions(question_text=question.question_text)
        self.db.add(db_question)
        self.db.commit()
        self.db.refresh(db_question)

        for choice in question.choices:
            db_choice = Choices(
                choice_text=choice.choice_text,
                is_correct=choice.is_correct,
                question_id=db_question.id
            )
            self.db.add(db_choice)
        
        self.db.commit()
        self.db.refresh(db_question)
        return db_question

    def delete_question(self, question_id: int):
        question = self.get_question(question_id)
        if question:
            self.db.delete(question)
            self.db.commit()
            return True
        return False
