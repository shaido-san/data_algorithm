class WaveletTree:
    def __init__(self, data, lo, hi):
        self.lo, self.hi = lo, hi
        self.map_left = []
        if lo == hi or not data:
            return
        mid = (lo + hi) // 2
        left, right = [], []
        for x in data:
            if x <= mid:
                left.append(x)
                self.map_left.append(1)
            else:
                right.append(x)
                self.map_left.append(0)
        # 累積に変換
        for i in range(1, len(self.map_left)):
            self.map_left[i] += self.map_left[i-1]
        self.left = WaveletTree(left, lo, mid)
        self.right = WaveletTree(right, mid+1, hi)

    # rank: [0..i) にある x の数
    def rank(self, x, i):
        if self.lo == self.hi:
            return min(i, len(self.map_left))
        mid = (self.lo + self.hi) // 2
        if x <= mid:
            return self.left.rank(x, self.map_left[i-1] if i else 0)
        else:
            return self.right.rank(x, i - (self.map_left[i-1] if i else 0))

    # kth smallest: 区間 [l, r) の中で k番目に小さい値
    def kth(self, l, r, k):
        if self.lo == self.hi:
            return self.lo
        inleft = self.map_left[r-1] - (self.map_left[l-1] if l else 0)
        if k <= inleft:
            return self.left.kth(self.map_left[l-1] if l else 0, self.map_left[r-1], k)
        else:
            return self.right.kth(l - (self.map_left[l-1] if l else 0),
                                  r - self.map_left[r-1], k - inleft)

arr = [3, 1, 4, 2, 4, 1, 3]
wt = WaveletTree(arr, min(arr), max(arr))

# rank: [0..5) に "1" が何個ある？
print(wt.rank(1, 5))  # → 2

# 区間 [2..7) にある 2番目に小さい値は？
print(wt.kth(2, 7, 2))  # → 3