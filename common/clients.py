import os
from anthropic import AsyncAnthropic
from dotenv import load_dotenv

load_dotenv()

def get_anthropic_client():
    """Creates and returns a global Anthropic client instance."""
    return AsyncAnthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
