#!/usr/bin/env python3
# -*- coding: utf-8 -*-

Z = lambda f: (lambda x: f(lambda y: x(x)(y)))(lambda x: f(lambda y: x(x)(y)))
sum_from_one = Z(lambda f: lambda n: f(n-1)+n if n else 0)
gcd = Z(lambda f: lambda a: lambda b: f(b)(a%b) if b else a)

print(sum_from_one(10))
print(gcd(12)(8))


true = lambda x: lambda y: x
false = lambda x: lambda y: y

Lif = lambda boolean: lambda M: lambda N: boolean(M)(N)
print(Lif(true)(True)(False))
print(Lif(false)(True)(False))

gcd_true = lambda x: lambda y: x(None)
gcd_bool = lambda x: gcd_true if x else false
gcd = Z(lambda f: lambda a: lambda b: Lif(gcd_bool(b))(lambda g: f(b)(a%b))(a))
print(gcd(12)(8))


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
print(GCD(12)(8))
