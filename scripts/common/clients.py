import os
from anthropic import AsyncAnthropic
from dotenv import load_dotenv
from common.config import ANTHROPIC_API_KEY

load_dotenv()

class Singleton(type):
    _instances = {}
    def __call__(class_, *args, **kwargs):
        if class_ not in class_._instances:
            class_._instances[class_] = super(Singleton, class_).__call__(*args, **kwargs)
        return class_._instances[class_]
    
class AnthropicClient(metaclass=Singleton):
    def __init__(self):
        self.client = AsyncAnthropic(api_key=ANTHROPIC_API_KEY)

    def get_client(self):
        return self.client

def get_anthropic_client():
    return AnthropicClient().get_client()