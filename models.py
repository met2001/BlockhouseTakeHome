from sqlalchemy import Column, Integer, String, Float
from database import Base

class Orders(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, unique=False)
    price = Column(Float)
    quantity = Column(Integer)
    order_type = Column(String)
    
    