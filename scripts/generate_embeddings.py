import os
import openai
import pandas as pd
import numpy as np
from tqdm import tqdm
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)

# Load a subset of data
df = pd.read_csv("email_dataset/train/train_emails.csv")
texts = df["clean_content"].dropna().sample(n=300, random_state=42)

# Keep the mapping between text and its index
texts.reset_index(drop=True, inplace=True)
texts_list = texts.tolist()

# Retrieve embeddings
print("📡 Fetching embeddings...")
embeddings = []

for text in tqdm(texts_list):
    try:
        response = client.embeddings.create(
            input=text[:2000],
            model="text-embedding-ada-002"
        )
        embeddings.append(response.data[0].embedding)
    except Exception as e:
        print(f"⚠️ Error: {e}")
        embeddings.append([0.0] * 1536)

# Save as .npy and .csv
np.save("email_dataset/train/embeddings_subset.npy", np.array(embeddings))
texts.to_csv("email_dataset/train/texts_subset.csv", index=False)

print("✅ Embeddings and texts saved!")
