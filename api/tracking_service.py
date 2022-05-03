from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import redis

app = FastAPI()
# start connection to redis server
r = redis.Redis(host='localhost', port=6379, db=0)

# defines a new game in request body
class StartGame(BaseModel):
    user_id: int
    game_id: int


@app.get("/start_game")
async def start_game():
    # try:
          
    # except Exception as e:
