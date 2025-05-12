def legendre(n, p):
    count = 0
    while n:
        n //= p
        count += n
    return count

print(legendre(100, 5))