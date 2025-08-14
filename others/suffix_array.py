def build_suffix_array(s):
    return sorted(range(len(s)), key=lambda i: s[i:])

text = "banana"
sa = build_suffix_array(text)
print("Suffix Array:", sa)

import bisect

def suffix_array_search(text, sa, pattern):
    n = len(text)
    m = len(pattern)

    l = bisect.bisect_left(sa, 0, key=lambda i: text[i:i+m] >= pattern)
    
    r = bisect.bisect_right(sa, 0, key=lambda i: text[i:i+m] > pattern)

    matches = [pos for pos in sa[l:r] if text[pos:pos+m] == pattern]
    return matches

print("検索 'ana':", suffix_array_search(text, sa, "ana"))