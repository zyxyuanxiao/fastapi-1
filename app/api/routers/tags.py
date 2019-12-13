from typing import List

from fastapi import APIRouter

from app.api.operation.tags import create_tag, get_tags
from app.schemas.tags import Tag, TagCreate

router = APIRouter()


@router.post("/add_tag/", response_model=Tag, tags=['tags'])
async def create_tags(tag: TagCreate):
    return await create_tag(tag.name)


@router.get("/tags/", response_model=List[Tag], tags=['tags'])
async def all_tags():
    return await get_tags()