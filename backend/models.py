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