from ast import While
from utils.recogniton import recognition
from utils.photo import take_picture
import time

n = 1

while True:
    take_picture(n)
    time.sleep(10)
