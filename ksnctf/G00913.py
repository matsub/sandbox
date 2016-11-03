#!/usr/bin/env python3
# coding: utf-8


def pi_prime(f):
    def sieve(n):
        s = list(range(n+1))
        for i in s[2:]:
            if s[i] == 0:
                continue
            for j in range(i*2, n+1, i):
                s[j] = 0
        return filter(lambda x: x, s[2:])

    digit = 10
    primes = list(sieve(100000))
    def is_prime(n):
        for prime in primes:
            if (n%prime)==0:
                return False
        return True

    pi = f.read()
    for head in range(len(pi)-digit):
        target = int(pi[head:head+digit])
        print(target)
        if is_prime(target):
            break
