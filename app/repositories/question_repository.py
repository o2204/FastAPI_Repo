from sqlalchemy.orm import Session
from app.models.question import Questions, Choices
from app.schemas.question import QuestionBase, ChoiceBase

class QuestionRepository:

    @staticmethod
    def get_question(db: Session, question_id: int):
        return db.query(Questions).filter(Questions.id == question_id).first()

    @staticmethod
    def create_question(db: Session, question: QuestionBase):
        db_question = Questions(question_text=question.question_text)
        db.add(db_question)
        db.commit()
        db.refresh(db_question)

        for choice in question.choices:
            db_choice = Choices(
                choice_text=choice.choice_text,
                is_correct=choice.is_correct,
                question_id=db_question.id
            )
            db.add(db_choice)

        db.commit()
        return db_question

    @staticmethod
    def delete_question(db: Session, question_id: int):
        question = QuestionRepository.get_question(db, question_id)
        if question:
            db.delete(question)
            db.commit()
            return True
        return False
