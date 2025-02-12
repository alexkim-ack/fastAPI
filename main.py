from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx

import constants

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

@app.get("/products")
async def products():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://fakestoreapi.com/products')
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")

@app.get("/categories")
async def categories():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://fakestoreapi.com/products/categories')
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")

@app.get("/category/{category}")
async def category(category: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://fakestoreapi.com/products/category/{category}")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")