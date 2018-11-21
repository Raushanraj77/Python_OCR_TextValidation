
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

print(pytesseract.image_to_string(Image.open('sample.png')))

if pytesseract.image_to_string(Image.open('sample.png')).find('vindication'):
        print('Text found...')