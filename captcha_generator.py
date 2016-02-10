#!/usr/bin/python3
#-*- coding: utf-8 -*-

__author__ = 'a2zh'

from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random

def rndChar():
    return chr(random.randint(65, 90))

def rndColor(rangeStart, rangeEnd):
    return (random.randint(rangeStart, rangeEnd), random.randint(rangeStart, rangeEnd), random.randint(rangeStart, rangeEnd))

def rndBgColor():
    return rndColor(64, 255)

def rndFgColor():
    return rndColor(32, 127)

width = 60 * 4
height = 60

fontPath = 'Hack-Regular.ttf'
fontSize = 36

image = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype(fontPath, fontSize)
draw = ImageDraw.Draw(image)

for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndBgColor())

for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font,
            fill=rndFgColor())

image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
