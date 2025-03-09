from anthropic import AsyncAnthropic
from anthropic.types.message import Message
from common.config import ANTHROPIC_MODEL


async def summarize_news_articles(
    articles: list[str], client: AsyncAnthropic
) -> list[str]:
    """
    Summarize a list of news articles using an anthropic model.

    Returns:
        list[str]: A list of summaries for the input news articles.
    """

    return [
        await summarize_news_article(article=article, client=client)
        for article in articles
    ]


async def summarize_news_article(article: str, client: AsyncAnthropic) -> str:
    """
    Summarize a news article using an anthropic model.

    Returns:
        (str): A summary of the input news article.
    """

    return (
        (
            await client.messages.create(
                max_tokens=1024,
                messages=[
                    {
                        "role": "user",
                        "content": f"Summarize the following news article and highlight key points:\n {article}",
                    }
                ],
                model=ANTHROPIC_MODEL,
                temperature=0.2,
            )
        )
        .content[0]
        .text
    )
