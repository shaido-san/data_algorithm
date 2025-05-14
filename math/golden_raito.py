def golden_raito_approx(n):
    a, b = 1, 1
    for i in range(n):
        a, b = a + b, a
    return a / b

for j in range(1, 11):
    print(f"Approx {j}: {golden_raito_approx(j)}")