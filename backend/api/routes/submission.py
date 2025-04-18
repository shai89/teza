from fastapi import APIRouter
from backend.controllers.submission_controller import handle_submission, get_last_submission
from backend.core.models import SubmissionIn, SubmissionOut
from backend.core.constants import HTTP_201_CREATED
router = APIRouter()

@router.post("/submissions", response_model=SubmissionOut, status_code=HTTP_201_CREATED)
def submit(submission: SubmissionIn):
    return handle_submission(submission)

@router.get("/submissions/last", response_model=SubmissionOut)
def last():
    return get_last_submission()
