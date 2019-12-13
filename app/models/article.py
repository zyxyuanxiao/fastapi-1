import orm

from app.db.basemodel import BaseModel
from app.db.database import database, metadata


class Tags(BaseModel):
    __tablename__ = 'tags'
    __database__ = database
    __metadata__ = metadata

    name = orm.String(max_length=255, allow_null=True)

    def __str__(self):
        return self.name


class Articles(BaseModel):
    __tablename__ = 'articles'
    __database__ = database
    __metadata__ = metadata

    title = orm.String(max_length=255, allow_null=True)
    views = orm.Integer(allow_null=True)
    content = orm.String(max_length=255, allow_null=True)
    tag_id = orm.ForeignKey(
        Tags,
        allow_null=True
    )

    def __str__(self):
        return self.title
