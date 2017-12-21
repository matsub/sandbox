#!/usr/bin/env python
# -*- coding: utf-8 -*-

class V:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __gt__(self, v):
        return self.a > v.a

    def __eq__(self, c):
        return self.b == v.b

    def __repr__(self):
        return f'({self.a}, {self.b})'

l = V(10, 3), V(20, 4), V(10, 5)

print(min(l))
print(l)
