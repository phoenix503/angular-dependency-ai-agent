from openai import AzureOpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

OPENAI_API_VERSION = os.getenv("OPENAI_API_VERSION")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")


def get_azure_openai_client():
    if not OPENAI_API_VERSION:
        raise ValueError("OPENAI_API_VERSION is not set")

    if not AZURE_OPENAI_ENDPOINT:
        raise ValueError("AZURE_OPENAI_ENDPOINT is not set")

    if not AZURE_OPENAI_API_KEY:
        raise ValueError("AZURE_OPENAI_API_KEY is not set")

    if not AZURE_OPENAI_ENDPOINT.startswith(("http://", "https://")):
        raise ValueError(
            "AZURE_OPENAI_ENDPOINT must start with http:// or https://"
        )

    # IMPORTANT: AzureOpenAI picks config from env internally
    return AzureOpenAI(
        api_key=AZURE_OPENAI_API_KEY,
        api_version=OPENAI_API_VERSION,
        azure_endpoint=AZURE_OPENAI_ENDPOINT
    )


def ai_recommend(package: str, current: str, target: str) -> str:
    """
    Uses Azure OpenAI Chat Completions to classify dependency upgrade risk.
    Always returns a string.
    """

    try:
        client = get_azure_openai_client()

        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Allowed: gpt-4o, gpt-4o-mini
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert Angular dependency upgrade advisor."
                },
                {
                    "role": "user",
                    "content": f"""
Package: {package}
Current version: {current}
Target version: {target}

Classify the upgrade risk as one of:
SAFE
REVIEW
UNSAFE

Give a one-line explanation.
"""
                }
            ],
            temperature=0.7,
            max_tokens=256,
            top_p=0.6,
            frequency_penalty=0.7
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"REVIEW: AI recommendation failed ({str(e)})"