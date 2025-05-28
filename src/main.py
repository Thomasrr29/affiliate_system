from src import Client, AssetBalance, Wallet #Importing the entities that have circular imports 
from fastapi import FastAPI 
from src.core.db import engine
from sqlmodel import SQLModel
from contextlib import asynccontextmanager
from src.api.api_v1 import api_router
from fastapi.middleware.cors import CORSMiddleware

async def create_tables(): 
    async with engine.begin() as conn: 
        await conn.run_sync(SQLModel.metadata.create_all)

@asynccontextmanager
async def lifespan(app: FastAPI):

    print("Running aplication and creating tables")

    await create_tables()
    yield 

app = FastAPI(lifespan=lifespan)

origins = [
    "http://127.0.0.1:5173", 
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(api_router, prefix="/api/v1")






