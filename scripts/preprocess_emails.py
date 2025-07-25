import pandas as pd
import re
from sklearn.model_selection import train_test_split
import os

# Function to remove metadata and clean text
def clean_text_advanced(text):
    # Remove technical headers
    text = re.sub(r'(?i)(message-id|date|from|to|subject|mime-version|content-type|content-transfer-encoding|x-[\w\-]+):.*?(?=\n|$)', '', text)

    # Remove all email addresses
    text = re.sub(r'\S+@\S+', '', text)

    # Remove URLs
    text = re.sub(r'http\S+', '', text)

    # Remove phone numbers
    text = re.sub(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', '', text)

    # Remove excessive blank lines
    text = re.sub(r'\n+', '\n', text)

    # Keep only email body — the part after the double newline
    split_parts = text.split('\n\n', 1)
    if len(split_parts) == 2:
        text = split_parts[1]
    
    # Final cleanup
    text = re.sub(r'\s+', ' ', text)
    return text.strip().lower()
    
# Load data
df = pd.read_csv('email_dataset/raw_data/emails.csv')

# Specify the column name that contains the original text with metadata
text_column = 'message'  # for example

# Drop rows with empty text
df = df.dropna(subset=[text_column])

# Apply the improved cleaning function
df['clean_content'] = df[text_column].apply(clean_text_advanced)

# Split into data sets
train_df, temp_df = train_test_split(df, test_size=0.3, random_state=42)
validation_df, test_df = train_test_split(temp_df, test_size=0.5, random_state=42)

# Save the processed data
for dataset, name in zip([train_df, validation_df, test_df], ['train', 'validation', 'test']):
    os.makedirs(f'email_dataset/{name}/', exist_ok=True)
    dataset.to_csv(f'email_dataset/{name}/{name}_emails.csv', index=False)

print("Data successfully processed and saved without metadata!")

