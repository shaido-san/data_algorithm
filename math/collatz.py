def collatz(n):
    steps = []
    while n != 1:
        steps.append(n)
        n = n//2 if n % 2 == 0 else 3 * n + 1
    steps.append(1)
    return steps
print(collatz(27))