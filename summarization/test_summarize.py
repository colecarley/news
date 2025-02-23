import asyncio
import os
from anthropic import AsyncAnthropic
from dotenv import load_dotenv

from summarization.utils.summarize import summarize_news_articles
from common.config import ANTHROPIC_API_KEY

client = AsyncAnthropic(
    api_key=ANTHROPIC_API_KEY,
)

if __name__ == "__main__":
    test_articles = ["""The U.S. economy added 943,000 jobs in July, the most since last August, and the unemployment rate fell to 5.4%, the Labor Department reported Friday. The job gains were the most since August 2020, when 1.6 million jobs were added. The unemployment rate fell from 5.9% in June. The job gains were driven by hiring in the leisure and hospitality, local government education, and professional and business services sectors. The labor force participation rate was unchanged at 61.7%.""",
                    """Bitcoin's price has surged to a three-month high, rising above $45,000 for the first time since May. The cryptocurrency's price has risen by more than 70% since hitting a low of $29,000 in July. The price surge comes as El Salvador prepares to adopt bitcoin as legal tender on September 7. The country's president, Nayib Bukele, has said that the move will help boost financial inclusion and economic growth in the country. The price of other cryptocurrencies, including Ethereum and Cardano, has also risen in recent days.""",]

    print(asyncio.run(summarize_news_articles(client=client, articles=test_articles)))