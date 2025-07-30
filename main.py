from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import select, Session

from database import get_db
from models import Question, Answer
from schemas import CreateQuestionRequest


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
)

@app.get("/questions")
async def get_questions(db: Session = Depends(get_db)) -> list[Question]:
    return db.exec(select(Question)).all()

@app.get("/questions/{question_id}")
async def get_question(question_id: int, db: Session = Depends(get_db)) -> Question:
    question: Question | None = db.get(Question, question_id)
    if question is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Question with ID {question_id} not found.")
    return question

@app.post("/questions", status_code=status.HTTP_201_CREATED)
async def create_question(create_question_request: CreateQuestionRequest, db: Session = Depends(get_db)) -> int:
    question: Question = Question(**create_question_request.model_dump())
    db.add(question)
    db.commit()
    db.refresh(question)
    return question.id