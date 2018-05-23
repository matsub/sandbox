#!/usr/bin/env python
# -*- coding: utf-8 -*-


def f(x):
    return x + 1


class Module:
    def __init__(self, rate=2):
        self.rate = rate

    def f(self, x):
        return x * self.x
