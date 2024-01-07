from pymongo import MongoClient
from flask import current_app
from dotenv import load_dotenv
import os

class MongoSingleton:
    _instance = None

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            if os.environ.get('MONGO_URL'):
                cls._instance = MongoClient(os.environ.get('MONGO_URL'))
            else:
                load_dotenv('.env/' + current_app.config["ENV"] )
                cls._instance = MongoClient(os.environ.get('MONGO_URL'))
        return cls._instance
