#!/usr/bin/env python
# coding: utf-8

'''http://www.pythonchallenge.com/pc/def/oxygen.html'''

import re
import urllib.request
from PIL import Image


def read(url):
    res = urllib.request.urlopen(url)
    img = Image.open(res)
    box = (0, 43, 608, 44)
    img = img.crop(box)
    rgb = img.convert("RGB")
    rgb_map = list(rgb.getdata())
    hint = ''.join(chr(i[0]) for i in rgb_map[::7])
    numitr = re.findall('[0-9]+', hint)
    return ''.join(chr(int(i)) for i in numitr)


if __name__ == '__main__':
    url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
    print(read(url))
