from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    email: str
    # created_at
    # updated_at
    total_solved: int
    total_failed: int

class Challenge(BaseModel):
    title: str
    answer: str
    provided_hints: str
    views: int
    fails: int
    created_by: User
    solved_by: User
    # publishd_status: Enum

# GET

@app.get("/")
async def root():
    return {"message": "Hello, world!"}

@app.get("/challenges")
async def challenges():
    return {"message": "challenges!"}

@app.get("/challenges/{id}")
async def challenge(id):
    return {"challenge_id": id}

@app.get("/user/{id}")
async def user(id):
    return {"user_id": id}


# POST

@app.post("/users/")
async def create_user(user: User):
    return user

@app.post("/challenges/")
async def create_challenge(challenge: Challenge):
    return challenge