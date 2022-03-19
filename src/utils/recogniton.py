from PIL import Image

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def recognition(filename):
    reading = pytesseract.image_to_string(
        filename, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    return reading
