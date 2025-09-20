import math

class SqrtDecomposition:
    def __init__(self, arr):
        self.n = len(arr)
        self.block_size = int(math.sqrt(self.n)) + 1
        self.arr = arr[:]
        self.blocks = [0] * self.block_size
        for i in range(self.n):
            self.blocks[i // self.block_size] += arr[i]

    def query(self, l, r):
        res = 0
        while l <= r and l % self.block_size != 0:
            res += self.arr[l]
            l += 1
        while l + self.block_size - 1 <= r:
            res += self.blocks[l // self.block_size]
            l += self.block_size
        while l <= r:
            res += self.arr[l]
            l += 1
        return res

    def update(self, i, val):
        block = i // self.block_size
        self.blocks[block] += val - self.arr[i]
        self.arr[i] = val

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9]
    sq = SqrtDecomposition(arr)

    print("query(2,7) =", sq.query(2,7))  # 3+4+5+6+7+8 = 33
    sq.update(4, 10)  # arr[4] = 10
    print("query(2,7) after update =", sq.query(2,7))  # 3+4+10+6+7+8 = 38