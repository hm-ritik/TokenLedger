from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.database import db
from sqlalchemy import text


@asynccontextmanager
async def lifespan(app:FastAPI):
    async with db.engine.connect() as conn:
        await conn.execute(text("SELECT 1"))
    yield


app=FastAPI(titile="Token Ledger" , lifespan=lifespan)



@app.get("/")
async def home():
    return {
        "Message" : "Health Api"
    }

@app.post("/")
async def make(name:str , rollno:int):
    return{
        "Message" : "I am writing you . These are testing Apis and I am setting up my project",
        "Nmae" : name ,
        "Rollno" :rollno
    }
