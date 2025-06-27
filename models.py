from pydantic import BaseModel


class Answer(BaseModel):
    response: str
    likes: int
    answered: bool
    user: str

class Question(BaseModel):
    title: str
    question: str
    topic: str | None
    likes: int = 0
    user: str
    answers: list[Answer] = []