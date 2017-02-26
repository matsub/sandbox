class Foo:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        i = 0
        while i < self.n:
            yield i
            i += 1

foo = Foo(10)
for i in foo:
    print(i)
