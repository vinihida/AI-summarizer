from fastapi import FastAPI
from app.api.routes.summaries import router as summaries_router

app = FastAPI(title="AI Summarizer")

app.include_router(summaries_router, prefix="/summaries")