from sqlmodel import SQLModel, create_engine, Session

DATABSE_URL = "sqlite:///./polls.db"
engine = create_engine(DATABSE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        # Yield closes the session after use
        yield session