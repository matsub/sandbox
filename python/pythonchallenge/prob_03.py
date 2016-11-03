#!/usr/bin/env python
# coding: utf-8

'''http://www.pythonchallenge.com/pc/def/equality.html'''

import re
import urllib.request


def decode(lines):
    s = ''.join(map(lambda l: l.decode(), lines))
    prog = re.compile('(?:[^A-Z]|^)[A-Z]{3}([a-z])[A-Z]{3}(?:[^A-Z]|$)')
    return ''.join(prog.findall(s))


if __name__ == '__main__':
    url = 'http://www.pythonchallenge.com/pc/def/equality.html'
    with urllib.request.urlopen(url) as res:
        lines = res.readlines()[21:-2]
        print(''.join(decode(lines)))
