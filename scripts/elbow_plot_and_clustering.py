import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from joblib import dump

# Load embeddings
embeddings = np.load("email_dataset/train/embeddings_subset.npy")
texts = pd.read_csv("email_dataset/train/texts_subset.csv")

# Elbow chart
print("📈 Plotting the elbow chart...")
inertias = []
k_values = range(2, 51, 2)

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(embeddings)
    inertias.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(k_values, inertias, marker='o')
plt.title("Elbow Method (OpenAI Embeddings + KMeans)")
plt.xlabel("Number of clusters (k)")
plt.ylabel("Inertia")
plt.grid(True)
plt.tight_layout()
plt.show()

# Additionally: save the KMeans model with the chosen k
k_opt = 12  # Set manually after inspecting the chart
final_kmeans = KMeans(n_clusters=k_opt, random_state=42)
texts["cluster"] = final_kmeans.fit_predict(embeddings)
texts.to_csv("email_dataset/train/texts_with_clusters.csv", index=False)

dump(final_kmeans, "models/kmeans_openai_embeddings.joblib")

print("Clusters saved. KMeans model stored in models/")

cluster_to_label = {
    "0": "Regulatory, Master Agreements & Credit Guidelines",
    "1": "Personal & Brief Work Messages",
    "2": "Legal & HR Communications",
    "3": "Counterparty Risk & Compliance Control",
    "4": "Operational Trade & Flow Accounting",
    "5": "Org Structure, Crisis Management & Recruiting",
    "6": "Project Finance & Contract Correspondence",
    "7": "Mass Marketing & Promotional Mailings",
    "8": "Forwarded General Content & Personal Notes",
    "9": "Meeting & Calendar Coordination",
    "10": "Work Files, Models & P&L Reporting",
    "11": "IT Notices, M&A Analytics & Industry Bulletins"
}

texts["category"] = texts["cluster"].map(cluster_to_label)
texts.to_csv("email_dataset/train/texts_with_labels.csv", index=False)

print("Clusters renamed to categories and saved.")
