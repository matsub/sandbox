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

    def see_instance(self):
        return self.__class__.l.msg


def decorator(f):
    def wrapped(*args, **kwargs):
        kwargs['extend'] = "whoaaaaaaaaa"
        return f(*args, **kwargs)
    return wrapped


class D:
    def __init__(self, value):
        self.value = value

    @decorator
    def method(self, extend):
        print(self.value)
        print(extend)


if __name__ == '__main__':
    # c = C('whoaaaaaaaa')
    # print(c.sum_of(3, 5))
    # print(c.see_instance())

    d = D('foooooooooo')
    d.method()
