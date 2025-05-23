def karatsuba(a, b):
    n = max(len(a), len(b))
    if n == 1:
        return [a[0] * b[0]]
    
    m = n // 2
    a += [0] * (n - len(a))
    b += [0] * (n - len(b))
    
    a_low, a_high = a[:m], a[m:]
    b_low, b_high = b[:m], b[m:]
    
    z0 = karatsuba(a_low, b_low)
    z2 = karatsuba(a_high, b_high)
    
    a_sum = [x + y for x, y in zip(a_low, a_high)]
    b_sum = [x + y for x, y in zip(b_low, b_high)]
    z1 = karatsuba(a_sum, b_sum)
    
    z1 = [z1[i] - z0[i] - z2[i] if i < len(z0) else z1[i] - z2[i] for i in range(len(z1))]
    
    result = [0] * (2 * n - 1)
    for i in range(len(z0)):
        result[i] += z0[i]
    for i in range(len(z1)):
        result[i + m] += z1[i]
    for i in range(len(z2)):
        result[i + 2 * m] += z2[i]
    
    return result

A = [1, 2, 3]  
B = [4, 5]     

result = karatsuba(A, B)
print("Result:", result)