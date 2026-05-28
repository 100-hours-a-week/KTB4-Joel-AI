from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.database import get_session
from app.models import Comment, Post
from app.schemas import (
    CommentCreate,
    CommentRead,
    CommentUpdate,
    PostCreate,
    PostRead,
    PostUpdate,
)


router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("", response_model=PostRead, status_code=201)
def create_post(post_create: PostCreate, session: Session = Depends(get_session)):
    post = Post.model_validate(post_create)
    session.add(post)
    session.commit()
    session.refresh(post)
    return post


@router.get("", response_model=list[PostRead])
def read_posts(session: Session = Depends(get_session)):
    return session.exec(select(Post).order_by(Post.id.desc())).all()


@router.get("/{post_id}", response_model=PostRead)
def read_post(post_id: int, session: Session = Depends(get_session)):
    post = session.get(Post, post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    post.view_count += 1
    session.add(post)
    session.commit()
    session.refresh(post)
    return post


@router.patch("/{post_id}", response_model=PostRead)
def update_post(
    post_id: int,
    post_update: PostUpdate,
    session: Session = Depends(get_session),
):
    post = session.get(Post, post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    
    update_data = post_update.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update")
    
    post.sqlmodel_update(update_data)
    session.add(post)
    session.commit()
    session.refresh(post)
    return post


@router.delete("/{post_id}", status_code=204)
def delete_post(post_id: int, session: Session = Depends(get_session)):
    post = session.get(Post, post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    comments = session.exec(select(Comment).where(Comment.post_id == post_id)).all()
    for comment in comments:
        session.delete(comment)

    session.delete(post)
    session.commit()


@router.post("/{post_id}/comments", response_model=CommentRead, status_code=201)
def create_comment(
    post_id: int,
    comment_create: CommentCreate,
    session: Session = Depends(get_session),
):
    post = session.get(Post, post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    comment = Comment.model_validate(comment_create, update={"post_id": post_id})
    post.comment_count += 1
    session.add(comment)
    session.add(post)
    session.commit()
    session.refresh(comment)
    return comment


@router.get("/{post_id}/comments", response_model=list[CommentRead])
def read_comments(post_id: int, session: Session = Depends(get_session)):
    post = session.get(Post, post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    return session.exec(
        select(Comment).where(Comment.post_id == post_id).order_by(Comment.id)
    ).all()


@router.patch("/comments/{comment_id}", response_model=CommentRead)
def update_comment(
    comment_id: int,
    comment_update: CommentUpdate,
    session: Session = Depends(get_session),
):
    comment = session.get(Comment, comment_id)
    if comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")

    update_data = comment_update.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update")

    comment.sqlmodel_update(update_data)
    session.add(comment)
    session.commit()
    session.refresh(comment)
    return comment


@router.delete("/comments/{comment_id}", status_code=204)
def delete_comment(comment_id: int, session: Session = Depends(get_session)):
    comment = session.get(Comment, comment_id)
    if comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")

    post = session.get(Post, comment.post_id)
    if post is not None and post.comment_count > 0:
        post.comment_count -= 1
        session.add(post)

    session.delete(comment)
    session.commit()
