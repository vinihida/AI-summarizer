from pydantic import BaseModel

class SummaryRequest(BaseModel):
    text: str

class SummaryResponse(BaseModel):
    job_id: str
    status: str
