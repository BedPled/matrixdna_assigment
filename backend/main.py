from fastapi import FastAPI
from pydantic import BaseModel
from backend.model.classifier import classify_email

app = FastAPI()

class EmailRequest(BaseModel):
    content: str

@app.post("/classify")
def classify(email: EmailRequest):
    category = classify_email(email.content)
    return {"category": category}
