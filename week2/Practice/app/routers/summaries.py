from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.database import get_session
from app.schemas import SummaryRead
from app.services.summary_service import summarize_post


router = APIRouter(prefix="/summaries", tags=["summaries"])


@router.post("/posts/{post_id}", response_model=SummaryRead)
def summarize_post_api(post_id: int, session: Session = Depends(get_session)):
    return summarize_post(post_id, session)
