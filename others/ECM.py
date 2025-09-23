import math
import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def inv_mod(a, n):
    # 拡張ユークリッド
    t, newt, r, newr = 0, 1, n, a
    while newr:
        q = r // newr
        t, newt = newt, t - q * newt
        r, newr = newr, r - q * newr
    if r > 1:
        return None
    return t % n

class EllipticCurve:
    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n

    def add(self, P, Q):
        if P is None: return Q
        if Q is None: return P
        x1,y1 = P
        x2,y2 = Q
        if x1 == x2 and (y1 + y2) % self.n == 0:
            return None
        if P != Q:
            num = (y2 - y1) % self.n
            den = (x2 - x1) % self.n
        else:
            num = (3*x1*x1 + self.a) % self.n
            den = (2*y1) % self.n
        g = gcd(den, self.n)
        if g > 1:
            raise ValueError(g)
        inv = inv_mod(den, self.n)
        if inv is None:
            raise ValueError(gcd(den, self.n))
        m = (num * inv) % self.n
        x3 = (m*m - x1 - x2) % self.n
        y3 = (m*(x1 - x3) - y1) % self.n
        return (x3,y3)

    def mul(self, P, k):
        R = None
        while k:
            if k & 1:
                R = self.add(R, P)
            P = self.add(P, P)
            k >>= 1
        return R

def ecm(N, B=50):
    while True:
        a = random.randrange(1, N)
        x = random.randrange(1, N)
        y = random.randrange(1, N)
        b = (y*y - x*x*x - a*x) % N
        E = EllipticCurve(a, b, N)
        P = (x,y)
        try:
            for k in range(2, B):
                P = E.mul(P, k)
        except ValueError as e:
            return e.args[0]

if __name__ == "__main__":
    N = 10403  # 101 * 103 の合成数
    factor = ecm(N, B=200)
    print("factor =", factor)
    print("N/factor =", N // factor)