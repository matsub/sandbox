#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class WrapClass:
    def __init__(self):
        self.bias = 10

    def instance_wrapper(self, cls):
        def decorator(f):
            def wrapper(*args, **kwargs):
                kwargs['value'] += self.bias
                return f(*args, **kwargs)
            return wrapper

        cls.func = decorator(cls.func)


class MethodClass:
    def func(self, value):
        return value*2


if __name__ == '__main__':
    wrapper = WrapClass()
    method = MethodClass()

    print("without changing:", method.func(value=10))

    wrapper.instance_wrapper(method)
    print("wrapped:", method.func(value=10))

    wrapper.bias = 100
    print("changed:", method.func(value=10))
