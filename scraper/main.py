import requests
from datetime import date 
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = "http://127.0.0.1:8000/"
API_KEY = os.getenv("API_KEY")

def get_categories() -> list[tuple[str, list[str]]]:
    response = requests.get(BASE_URL + "categories/")
    return list(map(lambda x: (x["name"], x["keywords"]), response.json()))

def create_url(keyword: str) -> str:
       return ("https://newsapi.org/v2/everything?"
              f"q={keyword}&"
              f"from={date.today().isoformat()}&"
              "sortBy=popularity&"
              f"apiKey={API_KEY}")

def get_related_articles(keywords: list[str]) -> list[str]:
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
              create_url(keyword)
              response = requests.get(create_url(keyword))
              json = response.json()

              if json["status"] == "ok":
                    content.extend(json["articles"])
              else:
                     print(f"Failed to fetch articles for {keyword}")
       return content

keywords_by_category_name = get_categories()
for category_name, keywords in keywords_by_category_name:
       articles = get_related_articles(keywords)
       # call the llm api to summarize the articles 
       
