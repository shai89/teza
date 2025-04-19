import os
import openai
import logging
from fastapi import HTTPException
from dotenv import load_dotenv
from pathlib import Path

from core.constants import (
    GPT_MODEL,
    GPT_TEMPERATURE,
    GPT_MAX_TOKENS,
    ERROR_MISSING_API_KEY,
    ERROR_OPENAI_FAILURE,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_502_BAD_GATEWAY,
)

# === Logger ===
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

load_dotenv()

DEFAULT_API_KEY = os.getenv("OPENAI_API_KEY")

if DEFAULT_API_KEY:
    logger.info(f"✅ OpenAI API Key Loaded: {DEFAULT_API_KEY[:8]}...")
else:
    logger.warning("❌ OpenAI API Key not found in environment!")


def generate_band_description(band: str, year: int, reason: str) -> str:
    """
    Generates a short description of a music band in a specific year using OpenAI's GPT.
    Falls back to default key from .env if not provided explicitly.
    Raises HTTPException on failure.
    """
    key = DEFAULT_API_KEY
    if not key:
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail=ERROR_MISSING_API_KEY
        )

    openai.api_key = key

    prompt = (
        f"Write two short paragraphs about the music group '{band}' and what happened in {year}. "
        f"Include the reason someone might like them: '{reason}'."
    )

    try:
        response = openai.ChatCompletion.create(
            model=GPT_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=GPT_TEMPERATURE,
            max_tokens=GPT_MAX_TOKENS,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logger.error(f"❌ GPT generation failed: {e}")
        raise HTTPException(
            status_code=HTTP_502_BAD_GATEWAY,
            detail=f"{ERROR_OPENAI_FAILURE}: {str(e)}"
        )

def generate_band_image_url(band: str, year: int, reason: str, api_key: str = None) -> str:
    """
    Uses OpenAI's DALL·E to generate an image URL related to the band.
    """
    key = api_key or DEFAULT_API_KEY
    if not key:
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail=ERROR_MISSING_API_KEY
        )

    openai.api_key = key
    
    prompt = f"{band} performing live in {year}, colorful and energetic"

    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512",
            response_format="url"
        )
        return response["data"][0]["url"]
    except Exception as e:
        logger.error(f"❌ Image generation failed: {e}")
        raise HTTPException(
            status_code=HTTP_502_BAD_GATEWAY,
            detail=f"{ERROR_OPENAI_FAILURE}: {str(e)}"
        )
