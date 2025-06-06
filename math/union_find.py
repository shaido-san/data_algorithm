class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # 各要素が自分自身を親とする
        self.rank = [0] * n  # 木の高さ（ランク）で最適化

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 経路圧縮
        return self.parent[x]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)

        if xroot == yroot:
            return  # すでに同じ集合

        # ランクの低い方を高い方にくっつける
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        else:
            self.parent[yroot] = xroot
            if self.rank[xroot] == self.rank[yroot]:
                self.rank[xroot] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

uf = UnionFind(10)
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(3, 4)

print(uf.connected(1, 6))  # True
print(uf.connected(1, 4))  # False