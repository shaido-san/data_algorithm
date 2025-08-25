import hashlib
import random

class CountMinSketch:
    def __init__(self, width=100, depth=5):
        self.width = width
        self.depth = depth
        self.table = [[0] * width for _ in range(depth)]
        self.seeds = [random.randint(0, 1e9) for _ in range(depth)]

    def _hash(self, x, seed):
        h = hashlib.md5((str(seed) + str(x)).encode()).hexdigest()
        return int(h, 16) % self.width

    def add(self, x, count=1):
        for i in range(self.depth):
            idx = self._hash(x, self.seeds[i])
            self.table[i][idx] += count

    def query(self, x):
        return min(
            self.table[i][self._hash(x, self.seeds[i])]
            for i in range(self.depth)
        )

cms = CountMinSketch(width=50, depth=5)

for ip in ["1.1.1.1", "2.2.2.2", "1.1.1.1", "3.3.3.3", "1.1.1.1"]:
    cms.add(ip)

print("1.1.1.1 の推定回数:", cms.query("1.1.1.1"))
print("2.2.2.2 の推定回数:", cms.query("2.2.2.2"))
print("4.4.4.4 の推定回数:", cms.query("4.4.4.4"))