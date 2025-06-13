from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
import os

MONGO_URL = os.getenv("MONGO_URL")
DB_NAME = os.getenv("DB_NAME")

client = AsyncIOMotorClient(MONGO_URL)
db = client[DB_NAME]

# Acesso direto às coleções
task_collection = db["tasks"]
category_collection = db["categories"]