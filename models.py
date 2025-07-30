from sqlmodel import Field, Relationship, SQLModel


class Answer(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    response: str
    likes: int
    answered: bool
    user: str
    question_id: int = Field(foreign_key="question.id")
    question: "Question" = Relationship(back_populates="answers")

class Question(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    title: str
    question: str
    topic: str | None
    likes: int = 0
    user: str
    answers: list[Answer] = Relationship(back_populates="question")