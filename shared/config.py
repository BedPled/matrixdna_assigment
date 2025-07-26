import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
FINE_TUNED_MODEL = "ft:gpt-3.5-turbo-1106:personal:email-classifier-v1:BxaDJEOF"