from dotenv import load_dotenv
from anthropic import AsyncAnthropic
from summarization.utils.summarize import summarize_news_articles, summarize_news_article
import os

load_dotenv() # Load environment variables from .env file

client = AsyncAnthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

def summarize_articles(articles: list[str]) -> list[str]:
    """
    Summarize a list of news articles using an anthropic model.

    Returns:
        list[str]: A list of summaries for the input news articles.
    """
    return summarize_news_articles(articles=articles, client=client)

def summarize_article(article: str) -> str:
    """
    Summarize a news article using an anthropic model.

    Returns:
        (str): A summary for the input news article.
    """
    return summarize_news_article(article=article, client=client)