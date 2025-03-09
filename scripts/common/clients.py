import os
from anthropic import AsyncAnthropic
from dotenv import load_dotenv

load_dotenv()

_anthropic_client = None


def get_anthropic_client():
    """Returns a single global instance of the Anthropic client."""
    global _anthropic_client
    if _anthropic_client is None:
        _anthropic_client = AsyncAnthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    return _anthropic_client
