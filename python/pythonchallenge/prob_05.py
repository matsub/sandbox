#!/usr/bin/env python
# coding: utf-8

'''http://www.pythonchallenge.com/pc/def/peak.html'''

import pickle
import urllib.request


def pick():
    url = 'http://www.pythonchallenge.com/pc/def/banner.p'
    res = urllib.request.urlopen(url)
    p = pickle.load(res)
    for cell in p:
        print(''.join(char*seq for char, seq in cell))


if __name__ == '__main__':
    pick()
