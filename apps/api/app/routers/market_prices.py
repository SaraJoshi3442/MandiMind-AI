from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..dependencies import get_db
from ..models.market_price import MarketPrice

router = APIRouter(
    prefix="/market-prices",
    tags=["Market Prices"]
)


@router.get("/")
def get_market_prices(db: Session = Depends(get_db)):
    prices = db.query(MarketPrice).all()
    return prices