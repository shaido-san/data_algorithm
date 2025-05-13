def pythagorean_triples(limit):
    triples = []
    for m in range(2, int(limit**0.5)+1):
        for n in range(1, m):
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            if c <= limit:
                triples.append((a, b, c))
    return triples

print(pythagorean_triples(30))