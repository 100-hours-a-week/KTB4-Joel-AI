from datetime import datetime, timezone

from sqlmodel import Field, Relationship, SQLModel


def get_now():
    return datetime.now(timezone.utc)


class Post(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    content: str
    author: str
    comment_count: int = 0
    view_count: int = 0
    created_at: datetime = Field(default_factory=get_now)

    comments: list["Comment"] = Relationship(back_populates="post")


class Comment(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    post_id: int = Field(foreign_key="post.id")
    content: str
    author: str
    created_at: datetime = Field(default_factory=get_now)

    post: Post | None = Relationship(back_populates="comments")
