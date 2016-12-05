#!/usr/bin/env python3
# -*- coding: utf-8 -*-

Z = lambda f: (lambda x: f(lambda y: x(x)(y)))(lambda x: f(lambda y: x(x)(y)))

true = lambda x: lambda y: x
false = lambda x: lambda y: y

_fact = Z(lambda f: lambda n: 1 if n==0 else n*f(n-1))
# print(_fact(5))

# church numeral
church2int = lambda n: n(lambda x: x+1)(0)
def int2church(n):
    if n == 0:
        return zero
    else:
        return succ(int2church(n-1))

zero = lambda f: lambda x: x
succ = lambda n: lambda f: lambda x: f(n(f)(x))
pred = (lambda n: lambda f: lambda x:
        n(lambda g: lambda h: h(g(f)))(lambda u: x)(lambda u: u)
        )
iszero = lambda n: n(lambda x: false)(true)
mult = lambda m: lambda n: lambda f: lambda x: n(m(f))(x)
add = lambda m: lambda n: lambda f: lambda x: n(f)(m(f)(x))


# fact with lambda
# fact = Z(lambda f: lambda n: iszero(n)(succ(zero))(mult(n)(f(pred(n)))))
def fact(n):
    b = iszero(n)(True)(False)
    if b:
        return succ(zero)
    else:
        return mult(n)(fact(pred(n)))
num = int2church(5)
print(church2int(fact(num)))
