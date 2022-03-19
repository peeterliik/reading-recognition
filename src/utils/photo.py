from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)


def take_picture(picname):
    camera.start_preview()
    sleep(2)
    camera.capture(picname)
