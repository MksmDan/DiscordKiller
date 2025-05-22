'''
Программа запускает FastApi
Эндпоинты:
    1 формирование бэкенд сервиса для работы с фронтом
    2 Формирование и выдача токенов
'''

from fastapi import FastAPI
from livekit import api
import os

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello Davitely"}


@app.get("/getToken")
def getToken():
    token = api.AccessToken(os.getenv('LIVEKIT_API_KEY'), os.getenv('LIVEKIT_API_SECRET')) \
        .with_identity("identity") \
        .with_name("name") \
        .with_grants(api.VideoGrants(
        room_join=True,
        room="my-room",
    )).to_jwt()

    return {"AccessToken": "asdfaeDSFSFQWFDFWas132#!@#$!#@"}
