class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def unite(self, x, y):
        self.parent[self.find(x)] = self.find(y)
    
    def same(self, x, y):
        return self.find(x) == self.find(y)

uf = UnionFind(10)
uf.unite(1, 2)
uf.unite(2, 3)
uf.unite(5, 6)

print(uf.same(1, 3))
print(uf.same(1, 5))
print(uf.find(3))