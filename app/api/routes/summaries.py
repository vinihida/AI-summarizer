import uuid
from fastapi import APIRouter, HTTPException
from app.api.schemas.summary import SummaryResponse, SummaryRequest
from app.services.queue_service import send_job
from app.services.storage_service import save_job, get_job

router = APIRouter()

@router.post("/", response_model=SummaryResponse)
def create_summary(request: SummaryRequest):
    job_id = str(uuid.uuid4())

    save_job(job_id, "PENDING")
    send_job(job_id)

    return SummaryResponse(job_id=job_id, status="PENDING")

@router.get("/job_id)", response_model=SummaryResponse)
def get_summary(job_id: str):
    job = get_job(job_id)

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    return SummaryResponse(
        job_id=job["job_id"],
        status=job["status"]
    )
