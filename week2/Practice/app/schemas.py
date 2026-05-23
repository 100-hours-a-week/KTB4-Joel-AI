from datetime import datetime
from sqlmodel import SQLModel


class PostCreate(SQLModel):
    title: str
    content: str
    author: str


class PostRead(PostCreate):
    id: int
    comment_count: int
    view_count: int
    created_at: datetime


class PostUpdate(SQLModel):
    title: str | None = None
    content: str | None = None


class CommentCreate(SQLModel):
    content: str
    author: str


class CommentRead(CommentCreate):
    id: int
    post_id: int
    created_at: datetime


class CommentUpdate(SQLModel):
    content: str | None = None


class SummaryRead(SQLModel):
    post_id: int
    provider: str
    summary: str
