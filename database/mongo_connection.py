from pymongo import MongoClient
from configuration import MONGO_URL, MONGO_CLIENT


client = MongoClient(MONGO_URL)

client.admin.command("ping")
db = client[MONGO_CLIENT]
users = db["popcorn_hunter_stats"]