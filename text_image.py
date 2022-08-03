from PIL import Image
from pytesseract import pytesseract

#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Define path to image
path_to_image = r'C:\Users\Lenovo\Documents\Projects\pic.jpg'

#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

#Open image with PIL
img = Image.open(path_to_image)

#Extract text from image
text = pytesseract.image_to_string(img)

print(text)









'''from tkinter.filedialog import askopenfile
import cv2
from pytesseract import pytesseract
from tkinter import *

oi=Tk()
oi.title("Text Extractor")
oi.geometry('500x500')
oi.resizable(0,0)
oi.config(bg="#081923",highlightcolor='white', highlightthickness=5)
def open_image():
    file = askopenfile(parent=oi, mode='rb', filetype=[("Image file", "*.png *.jpeg *jpg")])
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
  
# Opening the image & storing it in an image object
    img = cv2.imread(file)
  
# Providing the tesseract executable
# location to pytesseract library
    pytesseract.tesseract_cmd = path_to_tesseract
  
# Passing the image object to image_to_string() function
# This function will extract the text from the image
    text = pytesseract.image_to_string(img)
  
# Displaying the extracted text
    print(text[:-1])
open_image()
oi.mainloop()'''