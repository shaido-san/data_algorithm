def boyer_moore(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0:
        return []
    
    bad_char = {c: -1 for c in set(text)}
    for i in range(m):
        bad_char[pattern[i]] = i

    matches = []
    s = 0  
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            matches.append(s)
            s += m - bad_char.get(text[s + m], -1) if s + m < n else 1
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))
    return matches

text = "abacaabadcabacabaabb"
pattern = "abacab"
print(boyer_moore(text, pattern))