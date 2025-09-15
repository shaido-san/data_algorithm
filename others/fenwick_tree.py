class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0]*(n+1)

    def add(self, i, x):
        while i <= self.n:
            self.bit[i] += x
            i += i & -i

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        return self.sum(r) - self.sum(l-1)

if __name__ == "__main__":
    n = 6
    bit = FenwickTree(n)
    arr = [0, 2, 1, 3, 2, 1, 4]  # 1-indexed用
    for i in range(1, n+1):
        bit.add(i, arr[i])

    print("prefix sums:")
    for i in range(1, n+1):
        print(f"sum[1..{i}] =", bit.sum(i))

    print("range_sum(2,5) =", bit.range_sum(2,5))