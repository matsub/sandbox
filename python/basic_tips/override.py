class C:
    def __init__(self, v): self.v = v
    def __eq__(self, v): return self.v == v

l = [C(x) for x in range(10)]
print(l[3] == 3)
print(5 in l)
