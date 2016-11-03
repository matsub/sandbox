#!/usr/bin/env python
# coding: utf-8

'''http://www.pythonchallenge.com/pc/return/good.html'''

import json
from PIL import Image, ImageDraw


def show():
    first = json.load(open('first.json'))
    second = json.load(open('second.json'))
    img = Image.new("RGB", (640, 640))
    camvas = ImageDraw.Draw(img)
    camvas.line(first)
    camvas.line(second)
    img.show()


if __name__ == '__main__':
    show()
