#!/usr/bin/env python3
# codin: utf-8


# memoizing decorator
def memoize(function):
    def _memoize(*args, _cache={}):
        if args in _cache:
            return _cache[args]
        result = function(*args)
        _cache[args] = result
        return result
    return _memoize
