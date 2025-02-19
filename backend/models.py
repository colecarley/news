from pydantic import BaseModel

class Category(BaseModel):
    def __init__(self, name: str, keywords: list[str]):
        self.name = name
        self.keywords = keywords

class User(BaseModel):
    def __init__(self, name: str, email: str, frequency: int, categories: list[str]):
        self.name = name
        self.email = email
        self.frequency = frequency
        self.categories = categories

class Summarization(BaseModel):
    def __init__(self, summarization: str, link: str, timestamp: int, category: str):
        self.summarization = summarization
        self.link = link
        self.timestamp = timestamp
        self.category = category

