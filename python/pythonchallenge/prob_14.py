#!/usr/bin/env python
# coding: utf-8

'''http://www.pythonchallenge.com/pc/return/italy.html'''

from PIL import Image


def solve():
    img = Image.open('wire.png')
    res = Image.new("RGB", (100, 100))

    direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    head = 0
    x, y = 100, 99
    for i in range(200):
        d = direction[i%4]
        for j in range(100 - (i+1)//2):
            x += d[0]
            y += d[1]
            p = img.getpixel((head, 0))
            res.putpixel((x, y), p)
            head += 1

    res.show()


if __name__ == '__main__':
    solve()
