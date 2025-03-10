import asyncio
from anthropic import AsyncAnthropic
from common.config import DEV

async def summarize_news_article_cluster(articles: str, client: AsyncAnthropic) -> str:
    """
    Summarize a news article cluster using an Anthropic model.

    """

    response = await client.messages.create(
        model="claude-3-5-haiku-20241022" if DEV else "claude-3-5-sonnet-latest",
        max_tokens=1024,
        temperature=0.2,
        messages=[{"role": "user", "content": f"Summarize the following related news articles into one and highlight key points:\n\n{articles}"}],
    )

    # Extract summary text properly
    return "\n".join(content.text for content in response.content)

# Example usage:
# client = AsyncAnthropic(api_key="your_api_key")
# summary = asyncio.run(summarize_news_article_cluster(your_articles_text, client))
