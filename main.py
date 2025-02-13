import httpx

from datetime import timedelta
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

from constants import ACCESS_TOKEN_EXPIRE_MINUTES, FAKE_USERS_DB
from models import Token, User
from utils import authenticate_user, create_access_token, get_current_active_user

app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = authenticate_user(FAKE_USERS_DB, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@app.get("/users/me", response_model=User)
async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user

@app.get("/products")
async def products(_: Annotated[User, Depends(get_current_active_user)]):
    async with httpx.AsyncClient() as client:
        response = await client.get('https://fakestoreapi.com/products')
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")

@app.get("/categories")
async def categories(_: Annotated[User, Depends(get_current_active_user)]):
    async with httpx.AsyncClient() as client:
        response = await client.get('https://fakestoreapi.com/products/categories')
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")

@app.get("/category/{category}")
async def category(category: str, _: Annotated[User, Depends(get_current_active_user)]):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://fakestoreapi.com/products/category/{category}")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")