#!/usr/bin/env python
# coding: utf-8

'''http://www.pythonchallenge.com/pc/return/balloons.html'''

import gzip
import difflib


hex_to_bytes = lambda h: int(h, 16).to_bytes(1, byteorder="big")
def getlines(lines):
    for line in lines:
        split = filter(lambda x: x, line.split(' '))
        yield b''.join(map(hex_to_bytes, split))


def solve():
    gz = gzip.open("deltas.gz")
    deltas = gz.read().decode()

    left, right = [], []
    for line in deltas.split('\n'):
        left.append(line[:53])
        right.append(line[56:])

    added, reduced, same = [], [], []
    for line in difflib.ndiff(left, right):
        if '+' in line:
            added.append(line[2:])
        elif '-' in line:
            reduced.append(line[2:])
        else:
            same.append(line[2:])

    for i, bytesmap in enumerate((added, reduced, same)):
        img = open('delta_%s.png' % i, 'wb')
        img.writelines(getlines(bytesmap))
        img.close()


if __name__ == '__main__':
    solve()
