from pydantic import BaseModel

class Category(BaseModel):
    name: str
    keywords: list[str]

class User(BaseModel):
    name: str
    email: str
    frequency: int
    categories: list[str]
        

class Summarization(BaseModel):
    summarization: str
    link: str
    timestamp: int
    category: str
        
class NewsApiArticle(BaseModel):
    source: dict[str, str] # id, name
    author: str
    title: str
    description: str
    url: str
    urlToImage: str
    publishedAt: str
    content: str