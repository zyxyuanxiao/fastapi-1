from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from ..db.database import create_connection, disconnect
from app.api.routers.questions import router as questions_router
from app.api.routers.users import router as users_router
from app.api.routers.tags import router as tag_router
from app.api.routers.articles import router as articles_router
from app.api.routers.category import router as category_router

# app = FastAPI(__name__)


def generate_application() -> FastAPI:
    application = FastAPI(__name__)
    application.debug = True

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_event_handler("startup", create_connection)
    application.add_event_handler("shutdown", disconnect)

    application.include_router(
        questions_router, prefix="/quesitons"
    )
    application.include_router(
        users_router, prefix="/users"
    )
    application.include_router(
        tag_router, prefix="/tags"
    )
    application.include_router(
        articles_router, prefix="/articles"
    )
    application.include_router(
        category_router, prefix="/categorys"
    )

    return application


app = generate_application()
