from dotenv import load_dotenv
import os

load_dotenv()


# telegram data

TOKEN = os.environ.get("TOKEN")
ADMIN_ID = os.environ.get("ADMIN_ID")