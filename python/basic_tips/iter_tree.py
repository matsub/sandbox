#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import chain

class Node:
    def __init__(self, value, degree):
        self.value = value
        self.degree = degree
        self.children = []

    def __gt__(self, node):
        return self.size > node.size

    def __eq__(self, node):
        return self.value == value

    def __iter__(self):
        yield self.value
        children = chain.from_iterable(self.children)
        for child in children:
            yield child

    @property
    def size(self):
        size_of_children = (child.size for child in self.children)
        return sum(size_of_children, len(self.children))

    def add_child(self, node):
        if len(self.children) < self.degree:
            self.children.append(node)
            return self
        else:
            parent = min(self.children)
            return parent.add_child(node)

    def remove_child(self, value):
        def remove_from(node):
            for child in node.children:
                if child.value == value:
                    node.children.remove(child)
                    return node
                else:
                    return remove_from(child)
        return remove_from(self)


if __name__ == '__main__':
    tree = Node(0, 2)
    for i in range(1, 10):
        node = Node(i, 2)
        tree.add_child(node)

    print(*tree)
