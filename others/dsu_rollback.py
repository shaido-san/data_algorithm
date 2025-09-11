class DSURollback:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
        self.changes = []

    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            self.changes.append((-1,-1,-1,-1))
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.changes.append((y, self.parent[y], x, self.size[x]))
        self.parent[y] = x
        self.size[x] += self.size[y]
        return True

    def snapshot(self):
        return len(self.changes)

    def rollback(self, snap=None):
        if snap is None:
            snap = len(self.changes)-1
        while len(self.changes) > snap:
            y, py, x, sx = self.changes.pop()
            if y == -1:
                continue
            self.parent[y] = py
            self.size[x] = sx

if __name__ == "__main__":
    dsu = DSURollback(5)
    print("初期 parent:", dsu.parent)

    snap0 = dsu.snapshot()
    dsu.union(0,1)
    dsu.union(1,2)
    print("0,1,2 を連結:", dsu.parent)

    snap1 = dsu.snapshot()
    dsu.union(3,4)
    print("3,4 も連結:", dsu.parent)

    dsu.rollback(snap1)
    print("rollback to snap1:", dsu.parent)

    dsu.rollback(snap0)
    print("rollback to snap0:", dsu.parent)