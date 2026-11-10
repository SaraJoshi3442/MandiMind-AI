from sqlalchemy import Column, Integer, String, Date, Float
from ..database import Base


class MarketPrice(Base):
    __tablename__ = "market_prices"

    id = Column(Integer, primary_key=True, index=True)
    commodity = Column(String, nullable=False)
    state = Column(String, nullable=False)
    district = Column(String, nullable=True)
    market = Column(String, nullable=False)
    arrival_date = Column(Date, nullable=False)
    min_price = Column(Float, nullable=True)
    max_price = Column(Float, nullable=True)
    modal_price = Column(Float, nullable=False)