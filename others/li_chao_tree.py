class LiChaoTree:
    class Line:
        def __init__(self, a, b):
            self.a = a
            self.b = b
        def eval(self, x):
            return self.a * x + self.b

    def __init__(self, xmin, xmax):
        self.xmin = xmin
        self.xmax = xmax
        self.size = 1
        while self.size < xmax - xmin + 1:
            self.size <<= 1
        self.lines = [None] * (2 * self.size)

    def add_line(self, a, b, idx=1, l=None, r=None):
        if l is None:
            l, r = self.xmin, self.xmax
        new_line = self.Line(a, b)
        if self.lines[idx] is None:
            self.lines[idx] = new_line
            return
        mid = (l + r) // 2
        left_better = new_line.eval(l) < self.lines[idx].eval(l)
        mid_better = new_line.eval(mid) < self.lines[idx].eval(mid)
        right_better = new_line.eval(r) < self.lines[idx].eval(r)
        if mid_better:
            self.lines[idx], new_line = new_line, self.lines[idx]
        if l == r:
            return
        if left_better != mid_better:
            self.add_line(new_line.a, new_line.b, idx*2, l, mid)
        elif right_better != mid_better:
            self.add_line(new_line.a, new_line.b, idx*2+1, mid+1, r)

    def query(self, x, idx=1, l=None, r=None):
        if l is None:
            l, r = self.xmin, self.xmax
        if self.lines[idx] is None:
            return float("inf")
        res = self.lines[idx].eval(x)
        if l == r:
            return res
        mid = (l + r) // 2
        if x <= mid:
            return min(res, self.query(x, idx*2, l, mid))
        else:
            return min(res, self.query(x, idx*2+1, mid+1, r))

if __name__ == "__main__":
    tree = LiChaoTree(-10, 10)
    tree.add_line(2, 3)   # y = 2x+3
    tree.add_line(-1, 10) # y = -x+10
    tree.add_line(1, 0)   # y = x
    for x in range(-3, 4):
        print(f"x={x}, min y={tree.query(x)}")