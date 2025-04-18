from core.models import SubmissionIn, SubmissionOut
from services.storage_service import save_submission, load_last_submission
from services.gpt_service import generate_band_description, generate_band_image_url
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

def process_submission(submission: SubmissionIn) -> SubmissionOut:
    logger.info("📥 Received submission: %s", submission)

    # GPT text
    try:
        text = generate_band_description(
            band=submission.band,
            year=submission.year,
            reason=submission.reason
        )
    except Exception as e:
        logger.warning("⚠️ GPT text generation failed: %s", str(e))
        text = f"⚠️ GPT unavailable. Reason: {submission.reason}"

    # DALL·E image
    try:
        image_url = generate_band_image_url(
            band=submission.band,
            year=submission.year,
            reason=submission.reason
        )
    except Exception as e:
        logger.warning("⚠️ GPT image generation failed: %s", str(e))
        image_url = None

    result = SubmissionOut(
        **submission.dict(exclude={"openai_api_key"}),
        text=text,
        image_url=image_url,
        submitted_at=datetime.utcnow()
    )

    save_submission(result)
    return result


def get_last_submission_saved():
    return load_last_submission()
