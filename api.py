from fastapi import FastAPI

import postgres
import random
import string

string_length = 20
characters = string.ascii_letters + string.digits

def generate_session_token():
    session_token = ''.join(random.choices(characters, k=string_length))
    return session_token


app = FastAPI()

@app.post("/login")
def login():
    if(postgres.sign_in(name, password)):
        session_token = generate_session_token()
        return session_token

@app.post("/signup")
def signup():
    return

@app.get("/wishlist")
def wishlist():
    return
