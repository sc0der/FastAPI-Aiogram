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
        self.db_session = dbSession
        self.cityCrud = CityCrud(self.db_session)

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
        self.db_session = dbSession
        self.rubricCrud = RubricaCrud(self.db_session)
        self.urls = [base_url+"rubrics"]

    def generate_urls(self):
        return [base_url+"rubrics/"+str(rubric.uid) for rubric in self.rubricCrud.get_list()]

    async def fetch(self, url):
        print(url)
        async with self.session.get(url) as response:
            if response.status != 200:
                response.raise_for_status()
            response = await response.json()
            print(response)
            [self.rubricCrud.create(rubrica={
                "uid": rubrica['id'], "name": rubrica['name'], "slug": rubrica['slug']}) for rubrica in response]
            return "OK"

    async def fetch_all(self):
        tasks = []
        for url in self.urls:
            task = asyncio.create_task(self.fetch(url))
            tasks.append(task)
        results = await asyncio.gather(*tasks)
        return results


class FetchItems:

    def __init__(self, session, dbSession):
        self.session = session
        self.db_session = dbSession
        self.rubricCrud = RubricaCrud(self.db_session)
        self.urls = [base_url+"rubrics"]
