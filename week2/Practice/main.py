from fastapi import FastAPI

from app.database import lifespan
from app.routers.posts import router as posts_router
from app.routers.summaries import router as summaries_router

app = FastAPI(title="Board API", lifespan=lifespan)

app.include_router(posts_router)
app.include_router(summaries_router)


@app.get("/")
def root():
    return {"message": "Board API"}
