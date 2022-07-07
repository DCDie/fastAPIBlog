from fastapi import FastAPI

from config.routers import main_router

app = FastAPI(
    title="FastAPI Blog Example",
    description="This is a FastAPI Blog Example",
    version="0.1.0",
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

app.include_router(main_router, prefix="/api")
