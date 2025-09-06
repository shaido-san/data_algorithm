import random
from math import gcd

def is_probable_prime(n: int) -> bool:
    if n < 2:
        return False
    small_primes = [2,3,5,7,11,13,17,19,23,29]
    for p in small_primes:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        a %= n
        if a == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue
        for _ in range(s-1):
            x = (x * x) % n
            if x == n-1:
                break
        else:
            return False
    return True

def pollards_rho(n: int) -> int:
    if n % 2 == 0:
        return 2
    while True:
        x = random.randrange(2, n-1)
        c = random.randrange(1, n-1)
        y = x
        d = 1
        while d == 1:
            x = (x*x + c) % n
            y = (y*y + c) % n
            y = (y*y + c) % n
            d = gcd(abs(x - y), n)
        if d != n:
            return d

def factor(n: int, res: list):
    if n == 1:
        return
    if is_probable_prime(n):
        res.append(n)
        return
    d = pollards_rho(n)
    factor(d, res)
    factor(n // d, res)

def factorize(n: int):
    if n < 0:
        return [-1] + factorize(-n)
    res = []
    factor(n, res)
    res.sort()
    return res

if __name__ == "__main__":
    nums = [
        8051,
        10403,
        600851475143,
        2**61 - 1,
        10**18 + 3,
    ]
    for n in nums:
        fs = factorize(n)
        print(f"{n} = {' * '.join(map(str, fs))}")