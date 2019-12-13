from datetime import datetime

from orm import DateTime
from pydantic import BaseModel

from ..models.questions import QuestionChoices


class QuestionBase(BaseModel):
    created_at: datetime = None
    # created_at: DateTime = datetime.now()


class QuestionCreate(QuestionBase):
    question: QuestionChoices


class Question(QuestionBase):
    id: int
    question: str

    class Config:
        orm_mode = True
