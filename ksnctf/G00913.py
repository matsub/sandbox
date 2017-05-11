#!/usr/bin/env python3
# coding: utf-8


def sieve(n):
    s = list(range(n + 1))
    for i in s[2:]:
        if s[i] == 0:
            continue
        for j in range(i * 2, n + 1, i):
            s[j] = 0
    return filter(lambda x: x, s[2:])


def is_prime(n, primes):
    for prime in primes:
        if (n % prime) == 0:
            return False
    return True


def d_prime(digset):
    digit = 10
    primes = list(sieve(10**(digit // 2)))
    for head in range(len(digset) - digit):
        target = int(digset[head:head + digit])
        if is_prime(target, primes):
            yield target

if __name__ == '__main__':
    e = open('e').read()
    for i, v in enumerate(d_prime(e)):
        print(i, '%010d' % v)
