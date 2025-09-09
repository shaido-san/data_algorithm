class ConvexHullTrick:
    def __init__(self):
        self.lines = []  # (a, b)

    def bad(self, l1, l2, l3):
        return (l3[1]-l1[1])*(l1[0]-l2[0]) <= (l2[1]-l1[1])*(l1[0]-l3[0])

    def add_line(self, a, b):
        self.lines.append((a,b))
        while len(self.lines) >= 3 and self.bad(self.lines[-3], self.lines[-2], self.lines[-1]):
            self.lines[-2] = self.lines[-1]
            self.lines.pop()

    def query(self, x):
        while len(self.lines) >= 2 and self.lines[0][0]*x + self.lines[0][1] >= self.lines[1][0]*x + self.lines[1][1]:
            self.lines.pop(0)
        a,b = self.lines[0]
        return a*x + b

if __name__ == "__main__":
    cht = ConvexHullTrick()
    cht.add_line(2, 3)   # y = 2x + 3
    cht.add_line(-1, 10) # y = -x + 10
    cht.add_line(1, 0)   # y = x

    xs = [0,1,2,3,4,5]
    for x in xs:
        print(f"x={x}, min y={cht.query(x)}")