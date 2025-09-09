from fastapi import FastAPI
from .database import create_db_and_tables
from .routers import tasks

app = FastAPI(
    title="Tasks API",
    description="CRUD simples de tarefas com FastAPI + SQLModel",
    version="0.1.0",
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(tasks.router)

@app.get("/")
def root():
    return {"ok": True, "msg": "Tasks API rodando"}
