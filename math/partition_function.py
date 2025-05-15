def partition(n):
    if n == 0:
        return 1
    total = 0
    k = 1
    while True:
        pent1 = k * (3*k - 1) // 2
        pent2 = k * (3*k + 1) // 2
        if pent1 > n:
            break
        sign = -1 if k % 2 == 0 else 1
        total += sign * partition(n - pent1)
        if pent2 <= n:
            total += sign * partition(n - pent2)
        k += 1
    return total

print(partition(5))