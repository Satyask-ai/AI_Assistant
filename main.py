import os
from dotenv import load_dotenv
load_dotenv()
env = os.getenv("Open_AI_gpt_key")

from openai import OpenAI
