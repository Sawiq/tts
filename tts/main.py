from fastapi import FastAPI

from tts.db import create_db_and_tables
from tts.routers import projects


def on_startup():
    create_db_and_tables()


app = FastAPI()

app.include_router(router=projects.router, prefix="/projects", tags=["projects"])

app.add_event_handler("startup", on_startup)


@app.get("/")
async def root():
    return {"message": "HW"}
