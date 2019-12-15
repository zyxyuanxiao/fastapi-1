from pydantic import BaseModel


class BaseModelResponse(BaseModel):
    code: str = "0"
    msg: str = "success"
    data: dict