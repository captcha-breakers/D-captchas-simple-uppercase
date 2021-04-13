import os
import random

images = os.listdir("./data/")
images_show = random.sample(images, 100)

for i in images_show:
    print("<img src=\"./data/", i, "\" width=\"200\">", sep="")
