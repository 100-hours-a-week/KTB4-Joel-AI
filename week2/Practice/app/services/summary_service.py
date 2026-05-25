from fastapi import HTTPException
from sqlmodel import Session

from app.ai.prompt import build_prompt
from app.ai.summarizer import summarize
from app.models import Post
from app.schemas import SummaryRead


def summarize_post(post_id: int, session: Session):
    post = session.get(Post, post_id)

    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    prompt = build_prompt(post.title, post.content)
    provider, summary = summarize(prompt)

    return SummaryRead(post_id=post.id, provider=provider, summary=summary)
