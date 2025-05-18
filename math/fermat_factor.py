import math

def fermat_factor(n):
    if n % 2 == 0:
        return 2, n // 2  

    a = math.isqrt(n) + 1
    b2 = a*a - n
    while not math.isqrt(b2)**2 == b2:
        a += 1
        b2 = a*a - n
    b = math.isqrt(b2)
    return a - b, a + b

print(fermat_factor(5959))  