from pymongo import MongoClient
from dotenv import load_dotenv
import certifi
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(
    MONGO_URI,
    tls=True,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=30000
)

client.admin.command('ping')

db = client["smart_retail_ai"]

prediction_collection = db["predictions"]