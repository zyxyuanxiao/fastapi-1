from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from app.schemas import questions
from app.api.operation.question import get_question, create_question
from app.models.questions import QuestionChoices

router = APIRouter()


@router.post("/create_question/", response_model=questions.Question)
async def create_questions(question: QuestionChoices):
    obj = await get_question(question)
    if obj:
        raise HTTPException(
            status_code=400,
            detail="Question has been inserted !!"
        )

    return await create_question(question)
