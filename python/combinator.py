# coding: utf-8

Z = lambda f: (lambda x: f(lambda y: x(x)(y)))(lambda x: f(lambda y: x(x)(y)))
g = lambda f: (lambda n: (lambda x=0: (lambda y=1: f(n-1)(y)(x+y) if n else x)))
gcd = lambda f: (lambda a: (lambda b: f(b)(a%b) if b else a))

print(Z(g)(10)()())
print(Z(gcd)(12)(8))
