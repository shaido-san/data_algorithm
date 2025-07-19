import math

class MoAlgorithm:
    def __init__(self, data):
        self.data = data
        self.n = len(data)
        self.freq = [0] * (max(data) + 1)
        self.count = 0

    def add(self, index):
        val = self.data[index]
        self.freq[val] += 1
        if self.freq[val] == 1:
            self.count += 1

    def remove(self, index):
        val = self.data[index]
        self.freq[val] -= 1
        if self.freq[val] == 0:
            self.count -= 1

    def process_queries(self, queries):
        block_size = int(math.sqrt(self.n))
        queries = sorted(queries, key=lambda x: (x[0] // block_size, x[1]))
        
        res = [0] * len(queries)
        l, r = 0, -1

        for i, (ql, qr) in enumerate(queries):
            while r < qr:
                r += 1
                self.add(r)
            while r > qr:
                self.remove(r)
                r -= 1
            while l < ql:
                self.remove(l)
                l += 1
            while l > ql:
                l -= 1
                self.add(l)
            res[i] = self.count

        return res
    
arr = [1, 1, 2, 1, 3, 4, 5]
queries = [(0, 4), (1, 3), (2, 4)]  # 0-indexed
mo = MoAlgorithm(arr)
answers = mo.process_queries(queries)

for i, ans in enumerate(answers):
    print(f"Query {i+1}: {ans}")