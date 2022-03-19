from utils.recogniton import recognition
from utils.photo import take_picture
from db.db import insert_reading

try:
    take_picture('capture.jpg')
    reading = recognition('capture.jpg')
    insert_id = insert_reading(reading)
    print(insert_id)
except:
    print('Something when wrong with the cron_job')
