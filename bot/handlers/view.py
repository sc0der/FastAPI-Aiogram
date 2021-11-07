# here will be handles bot with db
from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:sc0der@localhost/somontj"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)


def updateAndSend():
    with engine.connect() as conn:
        result = conn.execute(
            '''SELECT * FROM items ORDER BY record_dt ASC LIMIT 10
                OFFSET (SELECT COUNT(*) FROM items) - 10;'''
        )
        for i in result:
            print((i.title))

        names = [item.title for item in result]
        return names


class ItemHandler:

    def __init__(self, engine):
        self.engine = engine

    def getLastItems(self):
        items = []
        with engine.connect() as conn:
            result = conn.execute(
                '''SELECT * FROM items ORDER BY record_dt ASC LIMIT 10
                    OFFSET (SELECT COUNT(*) FROM items) - 10;'''
            )
            items = result
        return items

    def getImageByItems(self, item_id):
        '''Returns images for current item'''
        images = []
        with engine.connect() as conn:
            result = conn.execute(
                f'''SELECT orig FROM images where item_id = {item_id}'''
            )
            images = result
        return images


    def getUserByItem(self, user_id):
        '''Returns author of current item'''
        users = []
        with engine.connect() as conn:
            result = conn.execute(
                f'''SELECT name, phone FROM users where uid = {user_id}'''
            )
            users = result
        return users[0]

    def getItemCityByID(self, city_id):
        citeis = []
        with engine.connect() as conn:
            result = conn.execute(
                f'''SELECT name FROM citeis where uid = {city_id}'''
            )
            citeis = result
        return citeis[0]