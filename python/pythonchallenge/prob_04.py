#!/usr/bin/env python
# coding: utf-8

'''http://www.pythonchallenge.com/pc/def/linkedlist.php'''

import re
import urllib.request


def crawl():
    baseurl = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
    NOTHING = lambda PARAM: '%s?nothing=%s' % (baseurl, PARAM)
    units = [
            'zero', 'one', 'two', 'three', 'four',
            'five', 'six', 'seven', 'eight', 'nine',
            '[0-9]+',
            ]
    p = re.compile('|'.join(units))

    code = '12345'
    match = p.search(code)
    while match:
        param = match.group()
        print(param)
        if param in units:
            param = units.index(param)
        res = urllib.request.urlopen(NOTHING(param))
        code = res.read().decode()
        match = p.search(code)

    return code


if __name__ == '__main__':
    print(crawl())
