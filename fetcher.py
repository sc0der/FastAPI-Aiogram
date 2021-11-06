import requests
import aiohttp
import asyncio
from models.database import crud, models, schemas
from models.database.crud import CityCrud, RubricaCrud
from sqlalchemy.orm import Session
from settings import *

class FetchCities:
    def __init__(self, session, dbSession):
        self.session = session
        self.dbSession = dbSession
        self.cityCrud = CityCrud(self.dbSession)

    async def paginations_urls(self, total_count):
        return [base_url+"cities/?page="+str(page) for page in range(1, int(total_count / 10)+2)]

    async def fetch(self, url):
        async with self.session.get(url) as response:
            if response.status != 200:
                response.raise_for_status()
            response = await response.json()
            [self.cityCrud.create(city={
                              "uid": city['id'], "name": city['name'], "slug": city['slug']}) for city in response["results"]]
            return "OK"

    async def fetch_all(self, urls):
        tasks = []
        for url in urls:
            task = asyncio.create_task(self.fetch(url))
            tasks.append(task)
        results = await asyncio.gather(*tasks)
        return results

class FetchRubrics:
    def __init__(self, session, dbSession):
        self.session = session
        self.dbSession = dbSession
        rubricCrud = RubricaCrud()
        
    async def fetch(self, url):
        async with self.session.get(url) as response:
            if response.status != 200:
                response.raise_for_status()
            response = await response.json()
            [crud.create(db=self.dbSession, city={
                              "uid": city['id'], "name": city['name'], "slug": city['slug']}) for city in response["results"]]
            return "OK"

    async def fetch_all(self, urls):
        tasks = []
        for url in urls:
            task = asyncio.create_task(self.fetch(url))
            tasks.append(task)
        results = await asyncio.gather(*tasks)
        return results