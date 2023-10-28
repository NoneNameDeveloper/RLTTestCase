from pymongo import MongoClient
from pymongo.database import Database

from app.data import Config

import logging

client: MongoClient = None


def get_db() -> Database:
	"""return db session"""
	return client[Config.MONGO_DB_NAME]


def init_db():
	"""initialize db"""
	global client

	try:
		client = MongoClient(Config.MONGO_URI)

		logging.info("Connected to mongo")

		return client[Config.MONGO_DB_NAME]
	except Exception as e:
		logging.exception(f"Cannot connect to mongo database: {e}")