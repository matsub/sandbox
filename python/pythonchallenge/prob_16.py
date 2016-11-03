#!/usr/bin/env python
# coding: utf-8

'''http://www.pythonchallenge.com/pc/return/mozart.html'''

from PIL import Image


def solve():
    img = Image.open("mozart.gif")
    camvas = Image.new("RGB", (1600, 1200))
    rgb = img.convert("RGB")
    line = []
    y = 0
    stack = 0
    for p in rgb.getdata():
        line.append(p)
        if p == (255, 0, 255):
            stack += 1
        if stack == 5:
            for x, lp in enumerate(line):
                camvas.putpixel((x, y), lp)
            stack = 0
            y += 1
            line = []
    camvas.show()


if __name__ == '__main__':
    solve()
