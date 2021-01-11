'''
 Goal: Write a script that pulls a random inspirational quote (potential: run through nlp model to get only inspirational ones; not important)
 - do not include dt

'''

from PIL import Image, ImageFont, ImageDraw
from config import creds
import requests
import sqlite3
from random import randint 


client = creds.connect_slack()


#choose image and font
# my_img = Image.open("../static/images/quote.png")
# text_font = ImageFont.truetype('../static/fonts/Lustria-Regular.ttf', 42.5)

# title_text = "The Beauty of Nature"
# image_editable = ImageDraw.Draw(my_img)
# image_editable.text((50, 200), title_text, fill = (255,255,255), font=text_font )
# my_img.save("../static/result.png")


class InspirationalQuote:
  pass

'''


response = requests.get('https://type.fit/api/quotes')
quotes = [quote['text'] for quote in response.json()]

quote_text = quotes[randint(0,len(quotes))]
author = "Elon Musk"

'''
