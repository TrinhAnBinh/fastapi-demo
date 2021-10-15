# main.py
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def hello():
    return {"message":"Wellcome to Binh.TrinhA Fast API demo"}