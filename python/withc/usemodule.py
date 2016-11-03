#!/usr/bin/env python3
# coding: utf-8

import ctypes as c
from ctypes import cdll


lib = cdll.LoadLibrary("module.so")

ab = c.c_int(1), c.c_int(2)
print("sum of 1 and 2 is %d" % lib.sum(*ab))

print("Hi Mr.Hankey!!")
lib.MrHankey(None)

class Vector(c.Structure):
    _fields_ = [("x", c.c_int), ("y", c.c_int)]

lib.scalar.restype = c.c_double
print("(3, 4)'s scalar is ", lib.scalar(Vector(3, 4)))
