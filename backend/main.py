import random
import string

# import uvicorn
import postgres
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

string_length = 20
characters = string.ascii_letters + string.digits


def generate_session_token():
    session_token = "".join(random.choices(characters, k=string_length))
    return session_token


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class LogIn(BaseModel):
    name: str
    password: str


@app.post("/login")
def login(data: LogIn):
    if postgres.sign_in(data.name, data.password):
        session_token = generate_session_token()
        postgres.session_token_to_db(session_token)
        return session_token


class SignUp(BaseModel):
    name: str
    password: str


@app.post("/signup")
def signup(data: SignUp):
    postgres.new_user(data.name, data.password)
    session_token = generate_session_token()
    postgres.session_token_to_db(session_token)
    return session_token


@app.get("/wishlist")
def wishlist():
    return


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="localhost", port=8000, reload=True)
