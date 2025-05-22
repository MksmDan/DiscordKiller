'''
Программа запускает FastApi
Эндпоинты:
    1 формирование бэкенд сервиса для работы с фронтом
    2 Формирование и выдача токенов
'''

from fastapi import FastAPI
from livekit import api
from pydantic import BaseModel
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello Davitely"}

class User(BaseModel):
    identity: str
    name: str
    room: str

# Обработчик POST-запроса
@app.post("/users/")
def create_user(user: User):
    token = api.AccessToken(os.getenv('LIVEKIT_API_KEY'), os.getenv('LIVEKIT_API_SECRET')) \
        .with_identity("identity") \
        .with_name("name") \
        .with_grants(api.VideoGrants(
        room_join=True,
        room="my-room",
    )).to_jwt()
    return {"message": f"Пользователь {user.name} создан", "user_data": user}

@app.post("/getToken")
def getToken(user: User):
    token = api.AccessToken("devkey",
                            "secret") \
        .identity = user.identity \
        .name = user.name \
        .with_grants(api.VideoGrants(
        room_join=True,
        room=user.room,
    )).to_jwt()

    return {"AccessToken": token}
