from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
from sqlalchemy import *
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)



def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

class Order(BaseModel):
    symbol: str = Field(min_length=1)
    price: float = Field(gt=0, lt=99999)
    quantity: int = Field(gt=0, lt=99999)
    order_type: str = Field(min_length=1)

@app.get("/orders")
def get_orders(db: Session = Depends(get_db)):
    return db.query(models.Orders).all()

@app.post("/orders")
def post_orders(order: Order, db: Session = Depends(get_db)):
    order_model = models.Orders()
    order_model.symbol = order.symbol
    order_model.price = order.price
    order_model.quantity = order.quantity
    order_model.order_type = order.order_type
    
    db.add(order_model)
    db.commit()
    
    return order
    
