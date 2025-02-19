from anthropic import AsyncAnthropic

async def summarize_news_articles(articles: list[str], client: AsyncAnthropic) -> list[str]:
    summaries = []
    for article in articles:
        response = await client.messages.create(
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": f"Summarize the following news article and highlight key points: {article}",
                }
            ],
            model="claude-3-5-sonnet-latest",
            temperature=0.2,
        )
        summaries.append(response.content)

    return summaries