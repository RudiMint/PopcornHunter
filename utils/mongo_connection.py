from pymongo import MongoClient
from utils.configuration import MONGO_URL, MONGO_CLIENT


client = MongoClient(MONGO_URL)

db = client[MONGO_CLIENT]
users = db["user_stats"]