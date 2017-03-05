class A:
    def test(self, a, b, c):
        return a, b, c

def overwrite(a):
    key = 'c'
    value = 'overwritten'

    def wrapper(f):
        def _wrapper(*args, **kwargs):
            if key not in kwargs: kwargs[key] = value
            return f(*args, **kwargs)
        return _wrapper

    a.test = wrapper(a.test)


if __name__ == '__main__':
    a = A()
    overwrite(a)
    print(a.test(1, 2))
    print(a.test(1, 2, c='origin'))
    # print(a.test(1, 2, 'duplicate'))
