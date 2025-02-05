from fastapi import FastAPI
from enum import Enum # 고유값 정의

class NickName(str, Enum):
    toad = "인서"
    rabbit = "시은"
    pig = "인서2"

app = FastAPI()

@app.get("/nicknames/{nick_name}") # api 파라미터 설정
async def get_name(nick_name : NickName): # 파라미터 타입 설정
    if nick_name is NickName.toad:
        return {"nick_name": nick_name, "message": "인서님 환영합니다."}
    elif nick_name is NickName.rabbit:
        return {"nick_name": nick_name, "message": "시은님 환영합니다."}
    elif nick_name is NickName.pig:
        return {"nick_name": nick_name, "message": "인서2님 환영합니다."}
        
# @app.get("/home_err/{name}")
# def read_name_err(name:int):
#     return {"name" : name}