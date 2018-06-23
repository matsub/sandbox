#!/usr/bin/env python
# -*- coding: utf-8 -*-

# s = \x -> \y -> \z -> x z (y z)
# k = \x -> \y -> x
# i = \x -> x

s = lambda x: lambda y: lambda z: x(z)( y(z) )
k = lambda x: lambda y: x
i = lambda x: x

# church bool
true = k
false = k(i)

# church numeral
zero = k(i)
