from time import sleep
from picamera import PiCamera
from PIL import Image
from skimage.color import rgb2gray
from skimage.io import imsave
from skimage import exposure

camera = PiCamera()
camera.resolution = (1024, 768)


def take_picture(picname):
    camera.start_preview()
    sleep(2)
    camera.capture(picname)
    camera.stop_preview()
    
    image = Image.open(picname)
    image = image.crop((100,493,689,676))
    image.save(picname)
    
    img = imread(picname)
    img_grey = rgb2gray(img)
    img_edited = exposure.adjust_gamma(img_grey, gamma=0.5, gain=1)
    
    imsave(picname, img_edited)
    
    
    