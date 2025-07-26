# scripts/prepare_finetune_jsonl.py
import pandas as pd
import json

# Load labeled data
df = pd.read_csv("email_dataset/train/texts_with_labels.csv")

# Remove rows without a category
df = df.dropna(subset=["category", "clean_content"])

# Limit text length (up to 2000 characters)
def truncate(text, max_chars=2000):
    return text[:max_chars]

# Write rows in JSONL format
with open("email_dataset/train/fine_tune_data.jsonl", "w") as f:
    for _, row in df.iterrows():
        example = {
            "messages": [
                {
                    "role": "system",
                    "content": "Classify the following email into one of the known categories based on its content. Only return the category name."
                },
                {
                    "role": "user",
                    "content": truncate(row["clean_content"])
                },
                {
                    "role": "assistant",
                    "content": row["category"]
                }
            ]
        }
        f.write(json.dumps(example) + "\n")

print("Fine‑tuning file prepared: fine_tune_data.jsonl")
