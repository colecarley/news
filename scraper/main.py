# STL
import requests
from datetime import datetime, date, timedelta, timezone
import os
import asyncio

# Third Party
from dotenv import load_dotenv

# Local
from summarization.main import summarize_articles, summarize_article
from scraper.utils import convert_news_api_timestamp_to_int
from backend.models import Summarization, Category

load_dotenv()

BASE_URL = "http://127.0.0.1:8000/"
API_KEY = os.getenv("API_KEY")

### ------------------- 1. Utility Functions ------------------- ###

def get_categories() -> list[tuple[str, list[str]]]:
    response = requests.get(BASE_URL + "categories/")
    return [(x["name"], x["keywords"]) for x in response.json()]

def create_news_api_url(keyword: str, days_ago: int = 1) -> str:
       return ("https://newsapi.org/v2/everything?"
              f"q={keyword}&"
              f"from={(date.today() - timedelta(days=days_ago)).isoformat()}&"
              "sortBy=popularity&"
              f"apiKey={API_KEY}")

def get_related_articles(keywords: list[str]) -> list[dict]:
       """response from news api
       {
       status: str,
       totalResults: int,
       articles: List[{
              source: {
                     id: str,
                     name: str
              },
              author: str,
              title: str,
              description: str,
              url: str,
              urlToImage: str,
              publishedAt: str,
              content: str
       }
       """

       content: list[str] = []
       for keyword in keywords:
              response = requests.get(create_news_api_url(keyword))
              json = response.json()

              if json["status"] == "ok":
                    content.extend(json["articles"])
              else:
                     print(f"Failed to fetch articles for {keyword}")
       return content

### ------------------- 2. Summarization & Storage ------------------- ###

async def send_summarization_to_backend(summary_obj: Summarization) -> None:
    """
    Send the summarized article to the backend via API.
    """
    try:
        print(f"JSON SUMMARY OBJ: {summary_obj.model_dump()}")
        response = await asyncio.to_thread(
            requests.post, f"{BASE_URL}/summarizations/create", json=summary_obj.model_dump()
        )
        if response.status_code == 200:
            print(f"Created summarization for: {summary_obj.link}")
        else:
            print(f"Failed to create summarization: {summary_obj.link} (Status: {response.status_code})")
    except Exception as e:
        print(f"Error sending summarization: {e}")

async def process_category(category_name: str, keywords: list[str]) -> None:
    """
    Process a news category: Fetch articles, summarize, and send to backend.
    """

    print(f"Processing category: {category_name}")

    articles = get_related_articles(keywords)
    
    if not articles:
        print(f"No articles found for category {category_name}")
        return

    # Select a subset of articles to avoid overwhelming the summarization API
    article_subset = articles[:3] # TODO: find a better way to handle this

    summaries = await summarize_articles(article_subset)

    summarization_objects = [
        Summarization(
            summarization=summaries[i], 
            link=article["url"],
            timestamp=convert_news_api_timestamp_to_int(article["publishedAt"]),
            category=category_name
        )
        for i, article in enumerate(article_subset)
    ]

    # Send summarizations to backend concurrently
    await asyncio.gather(*(send_summarization_to_backend(summary) for summary in summarization_objects))


### ------------------- 3. Main Script ------------------- ###
async def main():

    categories = get_categories()
    if not categories:
        print("No categories retrieved. Exiting.")
        return

    # TEST: Process a single category
    categories = categories[:1] # TODO: Remove this line

    # Process each category concurrently
    await asyncio.gather(*(process_category(name, keywords) for name, keywords in categories))

if __name__ == "__main__":
      asyncio.run(main())