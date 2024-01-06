from pymongo import MongoClient

class MongoSingleton:
    _instance = None

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = MongoClient("mongodb://admin:admin@localhost:27017")
        return cls._instance
