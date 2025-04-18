from fastapi import HTTPException
from core.models import SubmissionIn, SubmissionOut
from services.submission_service import process_submission, get_last_submission_saved
from core.constants import HTTP_404_NOT_FOUND

def handle_submission(submission: SubmissionIn) -> SubmissionOut:
    return process_submission(submission)

def get_last_submission() -> SubmissionOut:
    sub = get_last_submission_saved()
    if not sub:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No submission found")
    return sub
