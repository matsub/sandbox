dic = {
    'a': 10,
    'b': 'test',
    'c': 0.9,
}


class Dobj:
    def __init__(self, d):
        for k, v in d.items():
            self.__setattr__(k, v)


print(dir(dic))
print(dir(Dobj(dic)))
