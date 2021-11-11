from dotenv import load_dotenv
import os

load_dotenv()
# DB-constants
DB_NAME = os.environ.get("DB_NAME")
DB_PASS = os.environ.get("DB_PASS")
DB_USER = os.environ.get("DB_USER")

# URLS-constants
base_url = os.environ.get("BASE_URL")


# bot datas
ADMIN_ID = os.environ.get("ADMIN_ID")
TOKEN = os.environ.get("TOKEN")