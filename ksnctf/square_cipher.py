#!/usr/bin/env python3
# coding: utf-8

from PIL import Image


def convert(f):
    for l in f.readlines():
        for bit in l[:-1]:
            if bit.isupper():
                yield 0
            else:
                yield 255

def square_cipher(f):
    img = Image.new("L", (31, 31))
    img.putdata(tuple(convert(f)))
    img.show()


if __name__ == '__main__':
    with open('sc') as f:
        square_cipher(f)
