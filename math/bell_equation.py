import math

def solve_pell(N):
    a0 = int(math.sqrt(N))
    if a0 * a0 == N:
        return None  
    m, d, a = 0, 1, a0
    num1, num = 1, a
    den1, den = 0, 1

    while num*num - N*den*den != 1:
        m = d*a - m
        d = (N - m*m)//d
        a = (a0 + m)//d
        num1, num = num, a*num + num1
        den1, den = den, a*den + den1
    return num, den

print(solve_pell(13)) 