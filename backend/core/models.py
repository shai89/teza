from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class SubmissionIn(BaseModel):
    name: str
    band: str
    reason: str
    year: int
    openai_api_key: Optional[str] = None

class SubmissionOut(SubmissionIn):
    text: Optional[str] = None
    image_url: Optional[str] = None
    stats: Optional[dict] = None
    submitted_at: datetime = Field(default_factory=datetime.utcnow)
