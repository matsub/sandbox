#!/usr/bin/env python
# coding: utf-8

'''http://www.pythonchallenge.com/pc/def/ocr.html'''

import urllib.request


def read(lines):
    for line in lines:
        fetch = lambda c: c.isalpha()
        yield from filter(fetch, line.decode())


if __name__ == '__main__':
    url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
    with urllib.request.urlopen(url) as res:
        lines = res.readlines()[37:-2]
        print(''.join(read(lines)))
