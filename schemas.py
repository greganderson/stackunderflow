from pydantic import BaseModel


class CreateQuestionRequest(BaseModel):
    title: str
    question: str
    topic: str | None = None
    user: str