#!/usr/bin/env python

def deco(f):
    a = {'test': 10}
    def wrap(*args, **kwargs):
        if 'a' in kwargs: kwargs['a'].update(a)
        else: kwargs['a'] = a
        return f(*args, **kwargs)
    return wrap

@deco
def f(**opt):
  return opt


if __name__ == '__main__':
    print(f(a={'foo': True}))
    print(f())
