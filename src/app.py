from fastapi import FastAPI, HTTPException
from src.model import SentimentClassifier
from langchain_groq import ChatGroq
from pydantic import BaseModel

model = ChatGroq(model_name='llama-3.2-1b-preview', temperature=0)
sentiment_classifier = SentimentClassifier(model=model)

app = FastAPI(
    title="Hotel Review Analysis",
    description="Get fast and efficient sentiment analysis for hotel reviews.",
    version="0.1.0",
)

class ReviewInput(BaseModel):
    review: str

@app.post("/sentiment/", response_model=dict)
async def analyze_sentiment(review_input: ReviewInput):
    """
    Analyzes the sentiment of a hotel review.

    Args:
        review_input (ReviewInput): The hotel review text.

    Returns:
        dict: A dictionary containing the sentiment evaluation (positive, negative, or neutral).
    """
    try:
        sentiment = sentiment_classifier(review=review_input.review)
        return sentiment
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error analyzing sentiment: {str(e)}")


