import random

import jwt
from jwt.exceptions import PyJWTError
from fastapi import Depends
from fastapi.exceptions import HTTPException

from app.schemas import user
from app.models.users import User, ActivationCode
from app.models.questions import Questions
from app.services.jwt import hash_password, oauth2_scheme, SECRET_KEY, ALGORITHM


async def create_user(user_obj: user.UserCreate, question_id: int):
    question_obj = await Questions.objects.get(id=question_id)
    return await User.objects.create(username=user_obj.username, email=user_obj.email,
                                     question_id=question_obj, password=hash_password(user_obj.password), answers=user_obj.answers)


async def get_user_by_email(email: str):
    return await User.objects.filter(email=email).all()


async def get_user_by_id(id: int):
    return await User.objects.get(id=id)


async def get_user_info(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("email")
        if email is None:
            raise credentials_exception
    except PyJWTError:
        raise credentials_exception
    user = await get_user_by_email(email=email)
    if not user:
        raise credentials_exception
    return user[0]


def generate_code():
    code = ""
    for i in range(6):
        code += str(random.randint(0, 9))

    return code


async def save_code(user_id: int, code: str):
    user = await get_user_by_id(user_id)
    v_code = await ActivationCode.objects.filter(user_id=user).all()
    if v_code:
        await v_code[0].update(code=code)
    else:
        await ActivationCode.objects.create(user_id=user, code=code)
