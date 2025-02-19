from anthropic import AsyncAnthropic
from anthropic.types.message import Message

async def summarize_news_articles(articles: list[str], client: AsyncAnthropic) -> list[str]:
    """
    Summarize a list of news articles using an anthropic model.

    Args:
        articles (list[str]): A list of news articles to summarize.
        client (AsyncAnthropic): An instance of the AsyncAnthropic client.

    Returns:
        list[str]: A list of summaries for the input news articles.
    """
    summaries: list[Message] = []
    for article in articles:
        response = await client.messages.create(
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": f"Summarize the following news article and highlight key points:\n {article}",
                }
            ],
            model="claude-3-5-sonnet-latest",
            temperature=0.2,
        )
        summaries.append(response.content)

    return summaries