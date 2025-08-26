import numpy as np

class LSH:
    def __init__(self, dim, num_planes=10):
        self.num_planes = num_planes
        self.planes = np.random.randn(num_planes, dim)
        self.buckets = {}

    def _hash(self, vec):
        bits = (np.dot(self.planes, vec) > 0).astype(int)
        return ''.join(bits.astype(str))

    def add(self, vec, value):
        h = self._hash(vec)
        if h not in self.buckets:
            self.buckets[h] = []
        self.buckets[h].append((vec, value))

    def query(self, vec):
        h = self._hash(vec)
        return self.buckets.get(h, [])
        
lsh = LSH(dim=3, num_planes=8)

# ベクトルを登録
lsh.add(np.array([1, 0, 0]), "A")
lsh.add(np.array([0.9, 0.1, 0]), "B")
lsh.add(np.array([0, 1, 0]), "C")

candidates = lsh.query(np.array([0.95, 0.05, 0]))
print("候補:", candidates)