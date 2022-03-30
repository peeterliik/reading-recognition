from pymongo import MongoClient
import datetime

client = MongoClient('mongodb://localhost:27017')

db = client.water_meter

readings = db.readings


def insert_reading(reading):
    inserted_reading = {
        "value": reading,
        "time": datetime.datetime.utcnow(),
        "sent": False,
    }
    post_id = readings.insert_one(inserted_reading).inserted_id
    return post_id
