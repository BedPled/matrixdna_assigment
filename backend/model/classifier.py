from openai import OpenAI
from shared.config import OPENAI_API_KEY, FINE_TUNED_MODEL

# Create OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

def classify_email(text: str) -> str:
    response = client.chat.completions.create(
        model=FINE_TUNED_MODEL,
        messages=[
            {"role": "system", "content": "Classify the following email into one of the known categories. Only return the category name."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content.strip()
