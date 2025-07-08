import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modinv(a, m):
    # 拡張ユークリッド互除法で逆元を求める
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


class RSA:
    def __init__(self, p, q):
        if not (is_prime(p) and is_prime(q)):
            raise ValueError("p と q は素数でなければなりません")
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        self.e = 65537  # よく使われる公開指数
        if gcd(self.e, self.phi) != 1:
            raise ValueError("e と φ(n) は互いに素でなければなりません")
        self.d = modinv(self.e, self.phi)

    def encrypt(self, plaintext):
        return pow(plaintext, self.e, self.n)

    def decrypt(self, ciphertext):
        return pow(ciphertext, self.d, self.n)

    def display_keys(self):
        print("公開鍵 (n, e):", (self.n, self.e))
        print("秘密鍵 (d):", self.d)


# 使い方
p = 61
q = 53
rsa = RSA(p, q)
rsa.display_keys()

message = 42
cipher = rsa.encrypt(message)
print("暗号化されたメッセージ:", cipher)

decrypted = rsa.decrypt(cipher)
print("復号されたメッセージ:", decrypted)