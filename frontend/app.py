import streamlit as st
import requests

st.title("📧 Email Classifier (Fine-tuned GPT)")

email = st.text_area("Paste your email content:", height=300)

if st.button("Classify"):
    if not email.strip():
        st.warning("Please enter some email content.")
    else:
        with st.spinner("Classifying..."):
            response = requests.post(
                "http://localhost:8000/classify",
                json={"content": email}
            )
            if response.ok:
                st.success(f"📂 Category: {response.json()['category']}")
            else:
                st.error("❌ Error during classification.")
