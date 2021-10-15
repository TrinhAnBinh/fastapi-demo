# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Iterator, Optional
app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.get("/")
def hello():
    return {"message":"Wellcome to Binh.TrinhA Fast API demo"}

@app.post('/vnpost')
async def create_item(item: Item):
    return item