from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os 

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    #Wait explicit order for save in database dont finish any incomplete process 
    autoflush=False,
    #Doesnt send changes to database right away wait until the order  
    bind=engine,
    #We register the engine in the session it is like the commander 
    class_=AsyncSession
    #We config async 
)

async def get_db(): 

    async with SessionLocal() as db: 
        yield db