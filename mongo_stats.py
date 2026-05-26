from pymongo import MongoClient
from configuration import MONGO_URL

client = MongoClient(MONGO_URL)