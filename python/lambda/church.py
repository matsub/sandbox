#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# boolean
_if = lambda b: lambda t: lambda e: b(t)(e)
true = lambda x: lambda y: x
false = lambda x: lambda y: y

# integer
zero = lambda f: lambda x: x
iszero = lambda n: n(lambda x: false)(true)
leq = lambda m: lambda n: iszero(sub(m)(n))

# operator
succ = lambda n: lambda f: lambda x: f(n(f)(x))
pred = lambda n: lambda f: lambda x: n(lambda g: lambda h: h( g(f) ))(lambda y: x)(lambda y: y)

# converter
church = lambda n: zero if n==0 else succ(church(n-1))
unchurch = lambda cn: cn(lambda x: x+1)(0)

# calculus on church numeral
add = lambda m: lambda n: n(succ)(m)
mul = lambda m: lambda n: lambda f: m(n(f))
exp = lambda m: lambda n: n(m)
sub = lambda m: lambda n: n(pred)(m)
div = lambda m: lambda n: _if( leq(n)(m) )( succ( div(sub(m)(n))(n) ) )( zero )
rem = lambda m: lambda n: _if( leq(n)(m) )( rem(sub(m)(n))(n) )( zero )

a, b = map(church, (13, 12))
print(f"13 + 12 = { unchurch( add(a)(b) ) }")

a, b = map(church, (50, 12))
print(f"50 * 12 = { unchurch( mul(a)(b) ) }")

a, b = map(church, (2, 4))
print(f"2 ** 4 = { unchurch( exp(a)(b) ) }")

a, b = map(church, (16, 4))
print(f"16 - 4 = { unchurch( sub(a)(b) ) }")

a, b = map(church, (16, 4))
print(f"16 // 4 = { unchurch( div(a)(b) ) }")

a, b = map(church, (15, 4))
print(f"15 % 4 = { unchurch( rem(a)(b) ) }")

# euclid
