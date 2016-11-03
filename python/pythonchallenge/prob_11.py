#!/usr/bin/env python
# coding: utf-8

'''http://www.pythonchallenge.com/pc/return/5808.html'''

from PIL import Image


def show():
    img = Image.open('cave.jpg')
    width, height = img.size
    res = Image.new("RGB", (width//2, height//2))
    for y in range(0, height, 2):
        for x in range(0, width, 2):
            p = img.getpixel((x, y))
            res.putpixel((x//2, y//2), p)
    res.show()


if __name__ == '__main__':
    print(show())
