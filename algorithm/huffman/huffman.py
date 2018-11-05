# -*- coding: utf-8 -*-

from functools import total_ordering
from heapq import (
        heappush,
        heappop,
        )


@total_ordering
class Code:
    def __init__(self, byte, freq):
        self.byte = byte
        self.freq = freq
        self.has_children = False

    def __lt__(self, other):
        if isinstance(other, Code):
            return self.freq < other.freq
        return NotImplemented

class Node(Code):
    def __init__(self, zero, one):
        self.zero = zero
        self.one = one
        self.freq = zero.freq + one.freq
        self.has_children = True


def huffman(dic):
    '''make huffman tree'''
    heap = []

    for byte, freq in dic.items():
        heappush(heap, Code(byte, freq))

    while len(heap) >= 2:
        i = heappop(heap)
        j = heappop(heap)
        parent = Node(i, j)
        heappush(heap, parent)

    return heappop(heap)
