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

    # set up the user file, max height and width, and random background color for the image
    
    userFileSaved = "rectangle.png"
    MAX_W, MAX_H = (512, 512)
    rgbRes = randColor()

    #ask user for name and extract first initial
    
    initial = input("Enter your name to generate an image with your first initial: ")[0:1].upper()

    # create a new image and rectangle to fill the image with the random color selection
    
    newImage = Image.new('RGB', (MAX_W, MAX_H), "white")
    letsDraw = ImageDraw.Draw(newImage)
    letsDraw.rectangle(((MAX_W, MAX_H),(0,0)), fill = (rgbRes[0],rgbRes[1],rgbRes[2]))

    # create the finished product and write text, save to file
    
    theFont = ImageFont.truetype("sans-serif.ttf", 384)
    w, h = theFont.getsize(initial)
    letsDraw.text(((MAX_W - w)/2, (MAX_H - (h + 50))/2 ), initial, font = theFont, fill= "white")
    newImage.save(userFileSaved, "PNG")

    # wish the user well lol
    
    print("Thanks! Your image was saved to", userFileSaved, ". Take care!")
    
def randColor():
    rgbl = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    return tuple(rgbl)

# call main

main()
