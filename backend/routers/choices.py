from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from backend.database import get_session
from backend.schemas.choice_schema import ChoiceCreate, ChoiceRead
from backend.models import Choice, Question

router = APIRouter()

# Endpoint to add a choice for a question
@router.post("/add_choice/", response_model=ChoiceCreate)
def create_choice(choice_data: ChoiceCreate, session: Session = Depends(get_session)):
    # First we validate that the question exists
    question = session.get(Question, choice_data.question_id)

    if not question:
        raise HTTPException(status_code=404, detail="Unable to find question for provided question id")
    
    # Creating the Choice object
    choice = Choice(question_id=choice_data.question_id, choice_text=choice_data.choice_text)

    # Adding to the Database
    session.add(choice)
    session.commit()
    session.refresh(choice)

    return choice

# Endpoint to get all choices for a specific question
@router.get("/question/{question_id}/all_choices", response_model=list[ChoiceRead])
def get_all_choices(question_id: int, session: Session = Depends(get_session)):
    # Validate question id exists
    question = session.get(Question, question_id)
    
    if not question:
        raise HTTPException(status_code=404, detail="Question with question id {question_id} not found")

    # Fetch all the choices
    choices = session.exec(select(Choice).where(Choice.question_id == question.id)).all()

    return choices


# Endpoint to provide a vote for a choice 
@router.post("/choices/{choice_id}/vote", response_model=ChoiceRead)
def cast_vote(choice_id: int, session: Session = Depends(get_session)):
    # Validate the the choice is valid
    choice = session.get(Choice, choice_id)

    if not choice:
        raise HTTPException(status_code=404, detail="Choice not found")
    
    # Increment the vote count
    choice.votes += 1
    
    # Commit to session
    session.commit()
    session.refresh(choice)

    return choice