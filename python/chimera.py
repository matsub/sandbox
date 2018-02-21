#!/usr/bin/env python
# -*- coding: utf-8 -*-

def uni_to_int(u):
    return int(u.encode().hex(), 16)


def uniand(u1, u2):
    return (uni_to_int(u1) & uni_to_int(u2)).to_bytes(3, 'big').decode()


def strand(s1, s2):
    for u1, u2 in zip(s1, s2):
        yield uniand(u1, u2)


if __name__ == '__main__':
    print('生 & 死')
    print(uniand('生', '死'))

    print('live & dead')
    print(''.join(strand('live', 'dead')))
