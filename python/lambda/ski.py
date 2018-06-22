#!/usr/bin/env python
# -*- coding: utf-8 -*-

s = lambda x: lambda y: lambda z: x(z)( y(z) )
k = lambda x: lambda y: x
i = lambda x: x

true = k
false = k(i)

k i = (lambda x: lambda y: x)(i)
    = lambda y: i
    = lambda y: lambda x: x
    = lambda x: lambda y: y
