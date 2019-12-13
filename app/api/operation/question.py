from app.models.questions import Questions, QuestionChoices


async def create_question(question: QuestionChoices):
    return await Questions.objects.create(question=question.value)


async def get_question(question: QuestionChoices):
    print(type(question))
    return await Questions.objects.get(question=question.value)

async def del_question(id: int):
    await Questions.objects.delete(id)
    return {"Question has been deleted !"}
