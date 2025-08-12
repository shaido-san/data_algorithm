def z_function(s: str):
    n = len(s)
    Z = [0] * n
    l = r = 0
    for i in range(1, n):
        if i <= r:
            Z[i] = min(r - i + 1, Z[i - l])
        while i + Z[i] < n and s[Z[i]] == s[i + Z[i]]:
            Z[i] += 1
        if i + Z[i] - 1 > r:
            l, r = i, i + Z[i] - 1
    return Z

def find_occurrences(pattern: str, text: str):
    if not pattern:
        return list(range(len(text)+1))  
    sep = '\x00' 
    s = pattern + sep + text
    Z = z_function(s)
    m = len(pattern)
    res = []
    for i in range(m + 1, len(s)):
        if Z[i] == m:
            res.append(i - m - 1)  
    return res


text = "ababaabababa"
pattern = "ababa"
print(find_occurrences(pattern, text))  # → [0, 6]