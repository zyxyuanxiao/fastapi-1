from fastapi import Depends, APIRouter, Path, Query
from starlette.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas import user, token_sa
from app.services.authenticate import authenticate_user, create_access_token
from app.api.operation.users import create_user, get_user_by_email, get_user_info, get_user_by_id
from app.api.operation.question import get_question
from app.models.questions import QuestionChoices
from app.services.jwt import oauth2_scheme
from app.services.smtp import async_send_message

router = APIRouter()


@router.post("/create/", response_model=user.User, tags=['users'])
async def create_users(iuser: user.UserCreate, iquestion: QuestionChoices):
    ouser = await get_user_by_email(iuser.email)
    if ouser:
        raise HTTPException(
            status_code=400,
            detail="Email has been used !!"
        )
    # oquestion = await get_question(iquestion)
    return await create_user(iuser, 9)


@router.post("/login/", response_model=token_sa.Token, tags=['users'])
async def user_login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"email": user[0].email, "username": user[0].username})
    return {"token": access_token, "token_type": "bearer"}


@router.get("/info/", response_model=user.User, tags=['users'])
async def get_info(user: user.User = Depends(get_user_info)):
    return user


@router.get("/send/", tags=['users'])
async def send_email(user: user.UserActivated = Depends(get_user_info)):
    if user.is_active:
        return JSONResponse(content="账户已激活！")
    async_send_message.delay(id=user.id, email=user.email)
    return JSONResponse(content={"msg": "邮件已发送，请尽快激活您的账户", "code": 0})


@router.get("/activated/{id}", tags=['users'])
async def activate(id: int = Path(..., gt=0, title="账户id"), q: str = Query(..., alias="code", len=6)):
    user = await get_user_by_id(id=id)
    await user.update(is_active=1)
    return JSONResponse(content={"msg": "成功激活", "code": 0})
