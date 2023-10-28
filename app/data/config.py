import os

from dotenv import load_dotenv


load_dotenv()


class Config:
    MONGO_HOST = os.getenv("MONGO_HOST")
    MONGO_PORT = os.getenv("MONGO_PORT")

    MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")

    MONGO_URI = f"mongodb://{MONGO_HOST}:{MONGO_PORT}"

    BOT_TOKEN = os.getenv("BOT_TOKEN")
