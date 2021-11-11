from celery import Celery
import json
import asyncio
import aiohttp
import requests
from sqlalchemy.orm import Session
import requests
from settings import *
from celery.schedules import crontab
from bot.handlers.view import ItemHandler, SenderMediaData
from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:sc0der@localhost/somontj"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

app = Celery('worker', broker='redis://guest@localhost//')
app.conf.timezone = 'UTC'
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "see-you-in-ten-seconds-task": {
        "task": "worker.send_message",
        "schedule": 120.0
    }
}


@app.task
def send_message():
    requests.get(url="http://127.0.0.1:8000/fetch/items")
    service = ItemHandler(engine)
    sender = SenderMediaData(chat_id="@elonho_dar_Tojikiston", token=TOKEN, service=service)
    sender.run()
