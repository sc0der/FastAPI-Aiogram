from celery import Celery
import json
import requests
from sqlalchemy.orm import Session
import requests
from celery.schedules import crontab
from bot.handlers.view import ItemHandler
from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:sc0der@localhost/somontj"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

count = 0

bot_token = "1968503343:AAHHp5u_R0eTdFnbgUKe_gGKwcentNNcH8M"
your_telegram_id = 563792320

app = Celery('worker', broker='redis://guest@localhost//')
app.conf.timezone = 'UTC'
app.autodiscover_tasks()
def SendMessage(chat_id, parse_mode, msg):
    global count
    count += 1
    keyboard = json.dumps({'inline_keyboard':[[{"text":count,"callback_data":"clicked"}]]})
    data={'chat_id': chat_id, 'text': msg, 'parse_mode': parse_mode, 'reply_markup': keyboard}
    return requests.post(url="https://api.telegram.org/bot"+bot_token+"/sendMessage",data=data).json()
    

app.conf.beat_schedule = {
    "see-you-in-ten-seconds-task": {
        "task": "worker.send_message",
        "schedule": 20.0
    }
}

@app.task
def send_message():
    requests.get(url="http://127.0.0.1:8000/fetch/items")
    updater = ItemHandler(engine=engine)
    items = len(updater.getUnpublishedItems())
    SendMessage(your_telegram_id, "HTML", str(items))