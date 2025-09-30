import math

class VanEmdeBoas:
    def __init__(self, universe_size):
        self.u = universe_size
        self.min = None
        self.max = None
        if universe_size > 2:
            sqrt_u = int(math.ceil(math.sqrt(universe_size)))
            self.cluster = [VanEmdeBoas(sqrt_u) for _ in range(sqrt_u)]
            self.summary = VanEmdeBoas(sqrt_u)
        else:
            self.cluster = None
            self.summary = None

    def high(self, x): return x // int(math.ceil(math.sqrt(self.u)))
    def low(self, x): return x % int(math.ceil(math.sqrt(self.u)))
    def index(self, h, l): return h * int(math.ceil(math.sqrt(self.u))) + l

    def insert(self, x):
        if self.min is None:
            self.min = self.max = x
        else:
            if x < self.min:
                x, self.min = self.min, x
            if self.u > 2:
                h, l = self.high(x), self.low(x)
                if self.cluster[h].min is None:
                    self.summary.insert(h)
                self.cluster[h].insert(l)
            if x > self.max:
                self.max = x

    def member(self, x):
        if x == self.min or x == self.max:
            return True
        elif self.u <= 2:
            return False
        else:
            return self.cluster[self.high(x)].member(self.low(x))

# --- 動作確認 ---
veb = VanEmdeBoas(16)  # Universe [0..15]
for x in [2, 3, 10, 15]:
    veb.insert(x)

print(veb.member(10))  # True
print(veb.member(5))   # False
print("min:", veb.min, "max:", veb.max)