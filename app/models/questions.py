from enum import Enum

import orm

from ..db.basemodel import BaseModel
from ..db.database import database, metadata


class QuestionChoices(Enum):
    num1 = '你是谁'
    num2 = '你叫什么'
    num3 = '你想咋地'


class Questions(BaseModel):
    __tablename__ = 'questions'
    __database__ = database
    __metadata__ = metadata

    question = orm.String(max_length=100, allow_null=True)

    def __str__(self):
        return self.question
