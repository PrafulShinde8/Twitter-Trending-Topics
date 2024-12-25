import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

class MongoDB:
    def __init__(self):
        self.client = MongoClient(os.getenv('MONGO_URI'))
        self.db = self.client['twitter_trends']
        self.collection = self.db['trends']

    def insert_record(self, record):
        self.collection.insert_one(record)

    def get_latest_record(self):
        return self.collection.find().sort('_id', -1).limit(1)[0]