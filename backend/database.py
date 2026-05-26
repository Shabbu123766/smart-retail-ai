from pymongo import MongoClient


MONGO_URL = "mongodb+srv://shabbuparveen377_db_user:Shabbu123@aimlcluster.oi7jdsq.mongodb.net/?appName=AIMLCluster"


client = MongoClient(MONGO_URL)


db = client["retail_ai_db"]


prediction_collection = db["sales_predictions"]