# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Iterator, Optional
app = FastAPI()


class Item(BaseModel):
    Data: str
    SendDate: str
    SignData: str


@app.get("/")
def hello():
    return {"message":"Wellcome to Binh.TrinhA Fast API demo"}

@app.post('/vnpost')
async def create_item(item: Item):
    return item