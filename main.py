# main.py
import json
from fastapi import FastAPI
from pydantic import BaseModel
import requests

host_router = 'http://uatomis.homecredit.vn:5000/'
end_point_router = 'vnpost'
url = host_router + end_point_router

http_proxy = 'http://172.24.65.65:8080'
proxy_dict = { 
              "http"  : http_proxy, 
              "https" : http_proxy, 
            }

def call_api(data:str):
    res = requests.Session()
    response = res.post(url=url,json=data,proxies=proxy_dict)
    status_code = response.status_code
    response_text = response.json()
    return status_code, response_text

def send_request(new_data):
    host_router = 'http://uatomis.homecredit.vn:5000/'
    end_point_router = 'vnpost'
    url = host_router + end_point_router
    res = requests.post(url,json=new_data,proxies=proxy_dict)

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
    
    data = item.Data
    data_dict = json.loads(data)
    new_data = {
        "Data" : data_dict['ItemCode']
    }
    send_request(new_data)
    return item