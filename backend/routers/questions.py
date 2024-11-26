from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select, Session
from backend.database import get_session
from backend.models import Question

router = APIRouter()

@router.get("/questions/") 
def get_questions(session: Session = Depends(get_session)):
    questions = session.exec(select(Question)).all()

    if not questions:
        raise HTTPException(status_code=404, detail="Question not found")

    return questions

@router.get("/questions/{question_id}")
def get_question(question_id: int, session: Session = Depends(get_session)):
    question = session.get(Question, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question

@router.post("/questions/")
def create_question(question: Question, session: Session = Depends(get_session)):
    session.add(question)
    session.commit()
    session.refresh(question)
    return question
    