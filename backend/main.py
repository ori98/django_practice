from fastapi import FastAPI
from backend.database import engine
from backend.routers import questions, choices
from backend.models import SQLModel

app = FastAPI()

# Include the routers
app.include_router(questions.router)
app.include_router(choices.router)

# Create tables
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)