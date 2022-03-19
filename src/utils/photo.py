from qt_gl_preview import *
from picamera2 import *
import time

picam2 = Picamera2()
preview = QtGlPreview(picam2)
preview_config = picam2.preview_configuration()
capture_config = picam2.still_configuration()
picam2.configure(preview_config)


def take_picture(n):
    picname = "capture"+n+".jpg"
    picam2.start()
    time.sleep(2)
    picam2.switch_mode_and_capture_file(capture_config, picname)
