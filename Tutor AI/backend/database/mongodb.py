from pymongo import AsyncMongoClient
from core.config import settings
from fastapi import FastAPI
from contextlib import asynccontextmanager

client=AsyncMongoClient(settings.mongodb_url)
db=client[settings.mongodb_dbname]
async def dbConnect():
    await client.admin.command('ping')#Trigger a connection to the database
    return db
async def dbDisconnect():
    await client.close()
@asynccontextmanager
async def lifespan(app:FastAPI):
    await app.state.db=await dbConnect()
    try:
        yield
    finally:
        await dbDisconnect()

