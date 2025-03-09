import os
from anthropic import AsyncAnthropic
from dotenv import load_dotenv
from common.config import ANTHROPIC_API_KEY

load_dotenv()
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
class AnthropicClient(metaclass=Singleton):
    def __init__(self):
        self.client = AsyncAnthropic(api_key=ANTHROPIC_API_KEY)

    def get_client(self):
        return self.client

def get_anthropic_client():
    return AnthropicClient().get_client()