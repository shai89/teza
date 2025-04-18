# === OpenAI Settings ===
GPT_MODEL = "gpt-3.5-turbo"
GPT_TEMPERATURE = 0.7
GPT_MAX_TOKENS = 300

# === Error Messages ===
ERROR_MISSING_API_KEY = "Missing OpenAI API Key"
ERROR_OPENAI_FAILURE = "OpenAI generation failed"

# === HTTP Status Codes ===
from starlette.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_422_UNPROCESSABLE_ENTITY,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_502_BAD_GATEWAY,
)
