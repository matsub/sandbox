#!/usr/bin/env python
# coding: utf-8

'''http://www.pythonchallenge.com/pc/return/mozart.html'''

import re
import bz2
import urllib.parse
import urllib.request
import http.cookiejar
import xmlrpc.client


def preparation():
    cookie = http.cookiejar.CookieJar()
    cookierq = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(cookierq)

    baseurl = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
    NOTHING = lambda PARAM: '%s?busynothing=%s' % (baseurl, PARAM)
    p = re.compile('is ([0-9]+)')

    def busy(param):
        while True:
            res = opener.open(NOTHING(param))
            code = res.read().decode()
            yield list(cookie)[0].value
            match = p.search(code)
            if match is None:
                break
            param = match.group(1)
            print(param)

    raw_code = ''.join(busy('12345'))
    code = urllib.parse.unquote_to_bytes(raw_code.replace('+', ' '))
    return bz2.decompress(code).decode()


def call_mozarts_father():
    url = 'http://www.pythonchallenge.com/pc/phonebook.php'
    server = xmlrpc.client.ServerProxy(url)
    print(server.phone("Leopold"))


def tell_him():
    msg = "the flowers are on their way"
    cookie = http.cookiejar.CookieJar()
    cookierq = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(cookierq)
    url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'

    opener.open('http://www.pythonchallenge.com/pc/def/linkedlist.php')
    list(cookie)[0].value = msg
    res = opener.open(url)
    return res.read().decode()


if __name__ == '__main__':
    print(tell_him())
