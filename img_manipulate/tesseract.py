from PIL import Image
import pytesseract

picfile = '/home/huruhai/temp/python-scraping/Chapter16_ImageProcessingFiles/test.png'
print(pytesseract.image_to_string(Image.open(picfile)))
