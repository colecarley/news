# STL 
import requests
import asyncio
from collections import defaultdict
from anthropic import AsyncAnthropic # TODO: remove this
from dotenv import load_dotenv # TODO: remove this
import os # TODO: remove this

# Local
# from common.config import BASE_URL #TODO: use this instead

load_dotenv()

BASE_URL = "http://127.0.0.1:8000/"
client = AsyncAnthropic(api_key=os.getenv("ANTHROPIC_API_KEY")) # TODO remove this.


def get_db_summarizations(since: int) -> list[dict]:
    response = requests.get(BASE_URL + f"summarizations/since/{since}")
    return response.json()

def get_db_users() -> list[dict]:
    response = requests.get(BASE_URL + "users")
    return response.json()

async def personalize_news_summaries(user: dict, summaries: list[dict]) -> str:

    article_summaries_text ='\n\n'.join([f'Summarized News Article {i}: \n {s}' for i, s in enumerate(summaries, start=1)])

    return (await client.messages.create(
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": (f"""
                            You are an expert news editor. Your task is to craft a concise, engaging, and informative newsletter
                            based on the following article summaries. 
                            
                            The user is named: '{user["name"]}' and is interested in {", ".join(user["categories"])}.

                            **Guidelines:** 
                            - Provide a compelling headline for the newsletter. 
                            - Highlight key events, points, or developments.
                            - Summarize key points in a clear and engaging way.
                            - Group related topics together to maintain coherence. 
                            - Avoid redundant information. 
                            - Use a professional but friendly tone. 

                            **Article Summaries:** 
                            {article_summaries_text} 

                            Now, generate a well-structured newsletter summary that captures the most important insights.
                            """)
            }
        ],
        model="claude-3-5-sonnet-latest",
        temperature=0.2,
    )).content[0].text


async def main():
    # Get users from db
    users = get_db_users()
    if not users:
        print("No users found.")
        return
    print(f"Succesfully fetched {len(users)} users.")

    # Get summaries from the database
    summaries = get_db_summarizations(0)
    if not summaries:
        print("No summaries found.")
        return
    print(f"Succesfully fetched {len(summaries)} summaries.")

    # Group summaries by user's categories
    user_summaries = {}

    for user in users:
        user_summaries[user["email"]] = [summary for summary in summaries if summary["category"] in user["categories"]]
        print(f"Found {len(user_summaries[user["email"]])} summaries for {user["email"]}")
    

    users_to_process = [user for user in users if user["email"] in user_summaries]

    results = await asyncio.gather(*(
        personalize_news_summaries(user, user_summaries[user["email"]]) 
        for user in users_to_process
    ))

    for user, summary in zip(users, results):
        print(f"\n--- Personalized Newsletter for {user['name']} ({user['email']}) ---\n")
        print(summary)
        print("\n-----------------------------------------------------------\n")

if __name__ == "__main__":
    if __name__ == "__main__":
      asyncio.run(main())