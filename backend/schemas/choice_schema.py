from pydantic import BaseModel

class ChoiceCreate(BaseModel):
    question_id: int
    choice_text: str

class ChoiceRead(BaseModel):
    id: int
    question_id: int
    choice_text: str
    votes: int

    class Config:
        # Enables pydatic serializing to JSON
        orm_mode = True