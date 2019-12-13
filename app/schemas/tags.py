from pydantic import BaseModel


class TagBase(BaseModel):
    pass


class TagCreate(TagBase):
    name: str


class Tag(TagBase):
    id: int
    name: str

    class Config:
        orm_mode = True
