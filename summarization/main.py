import os

from summarization.utils.summarize import summarize_news_articles, summarize_news_article
from common.clients import get_anthropic_client

client = get_anthropic_client()

async def summarize_articles(articles: list[str]) -> list[str]:
    """
    Summarize a list of news articles using an anthropic model.

    Returns:
        list[str]: A list of summaries for the input news articles.
    """
    return await summarize_news_articles(articles=articles, client=client)

async def summarize_article(article: str) -> str:
    """
    Summarize a news article using an anthropic model.

    Returns:
        (str): A summary for the input news article.
    """
    return await summarize_news_article(article=article, client=client)