from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fetcher import *
from models.database import models, schemas
from models.database.crud import CityCrud
from models.database.database import SessionLocal, engine
import aiohttp
import asyncio

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def index(db: Session = Depends(get_db)):
    return {"msg": "bingo"}

@app.get("/cities")
def index(db: Session = Depends(get_db)):
    cityDB = CityCrud(db)
    cities = cityDB.get_list()
    return {"msg": cities}

async def fetchCities(db):
    async with aiohttp.ClientSession() as session:
        fetcher = FetchCities(session, db)
        urls = await fetcher.paginations_urls(66)
        await fetcher.fetch_all(urls)
        return "200"

async def fetchRubrics(db):
    async with aiohttp.ClientSession() as session:
        fetcher = FetchRubrics(session, db)
        await fetcher.fetch_all()
        return "200"

async def fetchSecondaryRubrics(db):
    async with aiohttp.ClientSession() as session:
        fetcher = FetchRubrics(session, db)
        fetcher.urls = fetcher.generate_urls()
        await fetcher.fetch_all()
        return "200"

@app.get("/fetch_cities")
def getCity(db: Session = Depends(get_db)):
    asyncio.run(fetchCities(db))
    return {"Result": "OK"}

@app.get("/fetch/rubrics")
def getCity(db: Session = Depends(get_db)):
    asyncio.run(fetchRubrics(db))
    return {"Result": "OK"}

@app.get("/fetch/rubrics/secondary")
def getCity(db: Session = Depends(get_db)):
    asyncio.run(fetchSecondaryRubrics(db))
    return {"Result": "OK"}