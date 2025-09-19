class Fenwick:
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

def cdq(points):
    def solve(l, r):
        if r - l <= 1:
            return
        m = (l+r)//2
        solve(l,m)
        solve(m,r)
        left = sorted(points[l:m], key=lambda p: p[1])
        right = sorted(points[m:r], key=lambda p: p[1])
        i = 0
        for px in right:
            while i < len(left) and left[i][1] <= px[1]:
                bit.add(left[i][2], 1)
                i += 1
            ans[px[3]] += bit.sum(px[2])
        for j in range(i):
            bit.add(left[j][2], -1)

    n = len(points)
    bit = Fenwick(max(p[2] for p in points)+2)
    ans = [0]*n
    solve(0,n)
    return ans

if __name__ == "__main__":
    pts = [(1,2,3,0),(2,3,4,1),(2,2,2,2),(3,3,3,3)]
    pts.sort(key=lambda p:p[0])
    ans = cdq(pts)
    for i,a in enumerate(ans):
        print(f"point {pts[i][:3]} is dominated by {a} points")