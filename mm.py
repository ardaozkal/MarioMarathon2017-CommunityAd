from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import requests

img = Image.open("img.png")
font = ImageFont.truetype("dosis.ttf", 40)
color = (255,255,255)
partner_name = "arqade.com"

draw = ImageDraw.Draw(img)

j = requests.get("http://www.mariomarathon.com/rest/partners/{}".format(partner_name)).json()

partner_total = "$" + str(j["domainTotal"])
total = "$" + str(round(j["total"]))

left_width = draw.textsize(total, font=font)[0]
draw.text((130 - (left_width / 2), 400),total,color,font=font)

right_width = draw.textsize(partner_total, font=font)[0]
draw.text((266 + 107 + (right_width / 2), 400),partner_total,color,font=font)
img.save('mmdyn.png')