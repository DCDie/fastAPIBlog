from fastapi import FastAPI

from config.routers import main_router

app = FastAPI()

app.include_router(main_router)
