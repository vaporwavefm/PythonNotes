# George Juarez

'''
    Image Generating Script
    Write a python script that takes a name and generates an image that contains the first letter of that name and a
    random color. The Pillow, random, and string modules will be useful to you.
    

'''
from PIL import Image, ImageFont, ImageDraw
import random

def main():
    
    # so this creates a new image?
    # idk im really confused by the Pillow module
    # I hope someone sees these comments and puts me on /ProgrammingHumor
    
    im = Image.new('RGB', (512,512), "white")
    dr = ImageDraw.Draw(im)
    dr.rectangle(((0,0),(10,10)), fill = "black", outline = "blue")
    im.save("rectangle.png")

    rgbRes = randColor()
    print(rgbRes[0], ",", rgbRes[1], ",", rgbRes[2])
    
def randColor():
    rgbl = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    return tuple(rgbl)

# call main

main()
