import os

import pypandoc
from fastapi import FastAPI
from api.logger import get_logger
from api.middlewares.cors import add_cors_middleware
from api.routes.chat_routes import chat_router
from api.routes.crawl_routes import crawl_router
from api.routes.explore_routes import explore_router
from api.routes.misc_routes import misc_router
from api.routes.upload_routes import upload_router
from api.routes.user_routes import user_router

logger = get_logger(__name__)
app = FastAPI()

add_cors_middleware(app)
max_brain_size = os.getenv("MAX_BRAIN_SIZE")
max_brain_size_with_own_key = os.getenv("MAX_BRAIN_SIZE_WITH_KEY",209715200)

@app.on_event("startup")
async def startup_event():
    pypandoc.download_pandoc()

app.include_router(chat_router)
app.include_router(crawl_router)
app.include_router(explore_router)
app.include_router(misc_router)
app.include_router(upload_router)
app.include_router(user_router)
