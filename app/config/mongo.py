from pymongo import MongoClient
from flask import current_app
from dotenv import load_dotenv
import os

class MongoSingleton:
    _instance = None

    @classmethod
    def get_instance(cls):
        load_dotenv('.env/' + current_app.config["ENV"] )
        if not cls._instance:
            cls._instance = MongoClient(os.environ.get('MONGO_URL'))
        return cls._instance
