#!/usr/bin/env python3

class Who(object):
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print('Hello %s.' % self.name)


def a():
    print('null')


def b():
    print('null')


def c():
    print('null')


def d():
    print('null')


def e():
    print('null')


def f():
    print('null')


def g():
    print('null null')


def h():
    print('null')


if __name__ == '__main__':
    who = Who('World')
    who.greeting()
