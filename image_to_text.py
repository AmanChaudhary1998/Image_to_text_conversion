import pytesseract
from PIL import Image
from gtts import gTTS
import os
import pyttsx3
from googletrans import Translator
img = Image.open('text.png')
print(img)
pytesseract.pytesseract.tesseract_cmd ='C:/Program Files (x86)/Tesseract-OCR/tesseract'
result = pytesseract.image_to_string(img)
with open('experiment.txt',mode='w') as file:
    file.write(result)
    print(result)
    file.close()

language='en'
output= gTTS(text=result,lang=language,slow=False)
output.save("output.mp3")
os.system("start output.mp3")

"""
p=Translator()
k=p.translate(result,dest='en')
engine=pyttsx3.init()
engine.say(k)
engine.runAndWait()
"""