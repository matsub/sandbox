#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Z-combinator
Z = lambda f: (lambda x: f(lambda y: x(x)(y)))(lambda x: f(lambda y: x(x)(y)))
sum_from_one = Z(lambda f: lambda n: f(n-1)+n if n else 0)
gcd = Z(lambda f: lambda a: lambda b: f(b)(a%b) if b else a)

# print(sum_from_one(10))
print(gcd(120)(80))


# boolean
true = lambda x: lambda y: x
false = lambda x: lambda y: y

# print(true(True)(False))
# print(false(True)(False))


# gcd with boolean
gcd_true = lambda x: lambda y: x(None)
gcd_bool = lambda x: gcd_true if x else false
gcd = Z(lambda f: lambda a: lambda b: gcd_bool(b)(lambda g: f(b)(a%b))(a))
# print(gcd(12)(8))


# likely only lambda
GCD = (lambda f:
    (lambda x:
        f(lambda y: x(x)(y))
    )(lambda x:
        f(lambda y: x(x)(y))
    )
)(lambda f: lambda a: lambda b:
    (lambda L: lambda M: lambda N:
        L(M)(N)
    )(
        (lambda L:
            (lambda x: lambda y: x(lambda x: x))
            if L else (lambda x: lambda y: y)
        )(
            b)
    )(lambda g:
        f(b)(a%b)
    )(a)
)
# print(GCD(12)(8))


# church numeral
zero = lambda f: lambda x: x

succ = lambda n: lambda f: lambda x: f(n(f)(x))
pred = lambda n: lambda f: lambda x: n(lambda g: lambda h: h(g(f)))(lambda y: x)(lambda x: x)

one = succ(zero)

church2int = lambda n: n(lambda x: x+1)(0)
def int2church(i):
    if i == 0:
        return zero
    else:
        return succ(int2church(i - 1))
# int2church = Z(lambda f: lambda n: (true if n==0 else false)(zero)(succ(f(n-1))))

num = int2church(13)
# print(church2int(num))


# calculus on church numeral
add = lambda m: lambda n: lambda f: lambda x: n(f)(m(f)(x))
mult = lambda m: lambda n: lambda f: lambda x: n(m(f))(x)
exp = lambda m: lambda n: n(m)
minus = lambda n: lambda m: m(pred)(n)
iszero = lambda n: n(lambda x: false)(true)
leq = lambda m: lambda n: iszero(minus(m)(n))

a, b = map(int2church, (13, 12))
# print(church2int(add(a)(b)))
a, b = map(int2church, (50, 12))
# print(church2int(mult(a)(b)))
