#!/usr/bin/env python
# coding: utf-8

'''http://www.pythonchallenge.com/pc/return/bull.html'''


def solve():
    def count_up(a):
        while a:
            head = a[0]
            tmp = a
            a = a.lstrip(head)
            amount = len(tmp) - len(a)
            yield str(amount)+head
    a = '1'
    for _ in range(30):
        a = ''.join(count_up(a))
    return len(a)


if __name__ == '__main__':
    print(solve())
