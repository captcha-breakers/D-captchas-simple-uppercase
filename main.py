from PIL import ImageFont, ImageDraw, Image
from random import random, choices, randint
import numpy as np
import cv2
import os
import sys
from string import ascii_uppercase  # , ascii_lowercase, digits
myfonts = [ImageFont.truetype(font="./fonts/"+i, size=35)
           for i in os.listdir("./fonts/")]

os.system("mkdir -p data")

n = int(sys.argv[1])  # Total captchas needs to be generated

for _ in range(n):
    img = np.zeros(shape=(70, 185, 3), dtype=np.uint8)
    img_raw = Image.fromarray(img+255)
    draw = ImageDraw.Draw(img_raw)
    font = myfonts[randint(0, len(myfonts)-1)]
    my_cap = ''.join(choices(ascii_uppercase, k=6))

    for i in range(6):
        draw.text((5+5*i+25*i, 10), my_cap[i], font=font, fill=(0, 0, 0))

    img = cv2.GaussianBlur(img,(5,5),0)
    img = np.array(img_raw)

    # # Adding noise
    # thresh = 0.02
    # for i in range(img.shape[0]):
    #     for j in range(img.shape[1]):
    #         rdn = random()
    #         if rdn < thresh:
    #             img[i][j] = 0
    #         elif rdn > 1-thresh:
    #             img[i][j] = 255

    cv2.imwrite("./data/"+my_cap+".png", img)

print(n, "captchas generated using", len(myfonts), "fonts at ./data/")