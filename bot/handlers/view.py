# here will be handles bot with db

import telebot
from telebot.types import *
import time

class ItemHandler:

    def __init__(self, engine):
        self.engine = engine

    def getUnpublishedItems(self):
        items = []
        with self.engine.connect() as conn:
            result = conn.execute(
                '''SELECT * FROM items where status = FALSE'''
            )
            items = [item for item in result]
            conn.close()
        return items

    def getLastItems(self):
        items = []
        with self.engine.connect() as conn:
            result = conn.execute(
                '''SELECT * FROM items ORDER BY record_dt ASC LIMIT 10
                    OFFSET (SELECT COUNT(*) FROM items) - 10;'''
            )
            items = result
            conn.close()
        return items

    def getImageByItems(self, item_id):
        '''Returns images for current item'''
        images = []
        with self.engine.connect() as conn:
            result = conn.execute(
                f'''SELECT * FROM images where item_id = {item_id}'''
            )
            for item in result:
                images.append(item['orig'])
            conn.close()
        return images

    def getUserByItem(self, user_id):
        '''Returns author of current item'''
        users = []
        with self.engine.connect() as conn:
            result = conn.execute(
                f'''SELECT name, phone FROM users where uid = {str(user_id)}'''
            )
            users = result
            conn.close()
        return users

    def getItemCityByID(self, city_id):
        cities = []
        with self.engine.connect() as conn:
            result = conn.execute(
                f'''SELECT name FROM cities where uid = {str(city_id)}'''
            )
            for item in result:
                cities.append(item['name'])
            conn.close()
        return cities

    def updateItemStatus(self, item_id):
        with self.engine.connect() as conn:
            conn.execute(
                f'''UPDATE items SET status = 'true' WHERE uid = {str(item_id)};'''
            )
            return "OK"
            conn.close()


class SenderMediaData:
    def __init__(self, chat_id, token, service):
        self.chat_id = chat_id
        self.token = token
        self.bot = telebot.TeleBot(self.token, parse_mode=None)
        self.item_service = service

    def items_list(self):
        return self.item_service.getUnpublishedItems()

    def getItemData(self, item):
        user = self.item_service.getUserByItem(item.uid)
        images = self.item_service.getImageByItems(item.user_id)
        return item, user, images

    def sendMessage(self, item):
        city = self.item_service.getItemCityByID(item['city_id'])
        images = self.item_service.getImageByItems(item['uid'])
        date = item['raise_dt'].split(',')
        media = []
        message = f"""🔎 {item['title']}  🔍
        {item['description']} \n
        💰*Цена: * {item['price']} \n
        🌐*Город: * {city[0]} \n
        💎*Торг: * {item['price_description']} \n
        📆*Дата: * {date[1]} \n
        👤*Имя: * {item['user_name']} \n 
        ☎️*Телефон: * {item['user_phone']}"""
        self.item_service.updateItemStatus(item['uid'])
        for item in range(len(images)):
            media.append(InputMediaPhoto(images[item], parse_mode='Markdown', caption = message if item == 0 else ''))            
        self.bot.send_media_group(self.chat_id, media=media)

    def run(self):
        if len(self.items_list()) > 0:
            for item in self.items_list():
                time.sleep(0.5)
                self.sendMessage(item)