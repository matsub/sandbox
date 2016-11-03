#!/usr/bin/env python
# coding: utf-8

'''http://www.pythonchallenge.com/pc/return/evil.html'''


def draw():
    evil = open('evil2.gfx', 'rb').read()
    types = ['jpg', 'png', 'gif', 'png', 'jpg']
    for i, ext in enumerate(types):
        f = open('dealed%d.%s' % (i, ext), 'wb')
        f.write(evil[i::5])
        f.close()


if __name__ == '__main__':
    draw()
