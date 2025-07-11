def modinv(a, m):
    # 拡張ユークリッド互除法で逆元を求める
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


class ChineseRemainderTheorem:
    def __init__(self, remainders, moduli):
        if len(remainders) != len(moduli):
            raise ValueError("余りと法の数が一致しません")
        self.remainders = remainders
        self.moduli = moduli

    def solve(self):
        total = 0
        prod = 1
        for m in self.moduli:
            prod *= m

        for r, m in zip(self.remainders, self.moduli):
            p = prod // m
            inv = modinv(p, m)
            total += r * inv * p

        return total % prod
    
remainders = [2, 3, 2]
moduli = [3, 5, 7]

crt = ChineseRemainderTheorem(remainders, moduli)
solution = crt.solve()

print("x ≡", solution, "mod", 3 * 5 * 7)  # x ≡ 23 mod 105