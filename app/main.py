from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "API funcionando no Railway!"}

@app.post("/sentiment")
def analyze_sentiment(request: TextRequest):
    analysis = TextBlob(request.text)
    polarity = analysis.sentiment.polarity  # de -1 (negativo) a 1 (positivo)
    subjectivity = analysis.sentiment.subjectivity  # de 0 a 1
    return {
        "text": request.text,
        "polarity": polarity,
        "subjectivity": subjectivity,
        "sentiment": "positivo" if polarity > 0 else "negativo" if polarity < 0 else "neutro"
    }
