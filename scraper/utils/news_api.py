import requests
from datetime import datetime, timezone

def convert_news_api_timestamp_to_int(timestamp: str) -> int:
    """
    Convert a NewsAPI Timestamp in format "YYYY-MM-DDTHH:MM:SSZ string into a Unix integer timestamp.
    """
    dt = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    return int(dt.timestamp())