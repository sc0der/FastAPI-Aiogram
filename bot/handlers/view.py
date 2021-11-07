# here will be handles bot with db
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
                f'''SELECT orig FROM images where item_id = {item_id}'''
            )
            images = result
            conn.close()
        return images

    def getUserByItem(self, user_id):
        '''Returns author of current item'''
        users = []
        with self.engine.connect() as conn:
            result = conn.execute(
                f'''SELECT name, phone FROM users where uid = {user_id}'''
            )
            users = result
            conn.close()
        return users[0]

    def getItemCityByID(self, city_id):
        citeis = []
        with self.engine.connect() as conn:
            result = conn.execute(
                f'''SELECT name FROM citeis where uid = {city_id}'''
            )
            citeis = result
            conn.close()
        return citeis[0]

    def updateItemStatus(self, item_id):
        with self.engine.connect() as conn:
            conn.execute(
                '''SELECT * from items where status = 'true';'''
            )
            return "OK"
            conn.close()