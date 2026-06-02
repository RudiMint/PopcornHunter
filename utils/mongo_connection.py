from pymongo import MongoClient
from utils.configuration import MONGO_URL, MONGO_CLIENT


client = MongoClient(MONGO_URL)

# client.admin.command("ping")
db = client[MONGO_CLIENT]
users = db["user_stats"]