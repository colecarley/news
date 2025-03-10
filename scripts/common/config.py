import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv(
    "BASE_URL", "http://127.0.0.1:8000/"
)  # Default to localhost if not set
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
DEV = True

SENTENCE_TRANSFORMER_EMBEDDING_MODEL = "all-MiniLM-L6-v2"
EMBEDDING_CHUNK_SIZE = 512 # Unique to embedding model: Refer to documentation
EMBEDDING_CHUNK_OVERLAP = 50