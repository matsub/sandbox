#!/usr/bin/env python3
# coding: utf-8

__author__ = "matsub.rk <matsub.rk@gmail.com>"
__version__ = "0.1"
__date__ = "02/February/2015"

def fizzbuzz(n):
    if not isinstance(n, int):
        raise TypeError(
            '\'%s\' object cannot be interpreted as an integer'
            % type(n).__name__)
    if n < 1:
        raise ValueError("Request Natural number.")

    for i in range(1, n+1):
        echo = ''
        if i % 3 == 0:
            echo += 'fizz'
        if i % 5 == 0:
            echo += 'buzz'
        if echo == '':
            echo = str(i)
        yield echo
