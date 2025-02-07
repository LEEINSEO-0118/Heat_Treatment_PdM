from fastapi import FastAPI
from enum import Enum # 고유값 정의
from pydantic import BaseModel

name_db = [{'인서' : 'toad'}, {'시은' : 'rabbit'}, {'하준' : 'giant'}]

app = FastAPI()

# get
@app.get("/names/{name_id}") # api 파라미터 설정
def get_name(name_id : str, skip : int = 0, limit : int = 10): # 파라미터 타입 설정
    return name_db[skip:skip+limit] # skip부터 skip+limit 까지의 데이터만 가져오기
  
@app.get("/")
def home_post():
    return {"hello" : "GET"}

class DataInput(BaseModel):
    name:str

# post
@app.post("/")
def home_post(data_request : DataInput):
    return {"hello" : "POST", "msg" : data_request.name}