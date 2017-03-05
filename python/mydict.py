dic = {
    'a': 10,
    'b': 'test',
    'c': 0.9,
}


class MyDict(dict):
    def __init__(self, dic):
        self.update(dic)
        for k, v in self.items():
            self.__setattr__(k, v)

    def echo(self):
        return dir(self)

d = MyDict(dic)
print(d, d.echo())
print('=== checking the id of values')
print('--- list of k/v of dictionary')
for k, v in d.items():
    print(id(k), id(v))

print('--- list of k/v of attr')
for k in d.keys():
    print(id(k), id(d.__getattribute__(k)))
