#!/usr/bin/env python3
# coding: utf-8


def square_cipher(f):
    foo = f.readline().replace('\n', '')
    for n, line in enumerate(f.readlines()):
        line = line.replace('\n', '')
        foo = [chr(ord(a)^ord(b)) for a, b in zip(foo, line)]
    print(''.join(foo))
