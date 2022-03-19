from pymongo import MongoClient
import datetime

client = MongoClient('mongodb://localhost:27017')

db = client.water_meter

readings = db.readings

reading = {
    "value": 78123,
    "time": datetime.datetime.utcnow()
}

post_id = readings.insert_one(reading).inserted_id
