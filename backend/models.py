from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from datetime import datetime

class Question(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    question_text: str 
    pub_date: datetime = Field(default_factory=datetime.utcnow)
    choices: list["Choice"] = Relationship(back_populates="question")

class Choice(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    choice_text: str
    votes: int = 0
    question_id: int = Field(foreign_key="question.id")
    question: Question | None = Relationship(back_populates="choices")