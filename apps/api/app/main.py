from .database import Base, engine
from .models.market_price import MarketPrice

Base.metadata.create_all(bind=engine)

from fastapi import Depends, FastAPI
from .dependencies import get_db

app = FastAPI(
    title="MandiMind AI",
    description="MandiMind AI is an AI-powered platform that provides insights and analysis for the agricultural industry. It leverages advanced machine learning algorithms to help farmers make informed decisions, optimize crop yields, and improve overall farm management.",
    version="1.0.0",
)

@app.get("/")
def home():
    return {"message": "Welcome to MandiMind AI!",
            "status": "API is running successfully."}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/test-db")
def test_db(db = Depends(get_db)):
    return {
        "message": "Database session provided successfully!"
    }