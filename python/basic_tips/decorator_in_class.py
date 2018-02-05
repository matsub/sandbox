#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Loud:
    def __init__(self, msg):
        self.msg = msg

    def deco(self, f):
        def wrapped(*args, **kwargs):
            print(self.msg)
            return f(*args, **kwargs)
        return wrapped


class C:
    l = Loud('niceeeee')

    def __init__(self, msg):
        self.l = Loud(msg)

    @l.deco
    def sum_of(self, x, y):
        return x + y

    @l.deco
    def diff_of(self, x, y):
        return x - y


if __name__ == '__main__':
    c = C('whoaaaaaaaa')
    print(c.sum_of(3, 5))
    print(c.diff_of(3, 5))
