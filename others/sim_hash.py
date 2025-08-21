import hashlib

def simhash(tokens, hashbits=64):
    v = [0] * hashbits
    for t in tokens:
        # 単語をハッシュ化
        h = int(hashlib.md5(t.encode("utf-8")).hexdigest(), 16)
        for i in range(hashbits):
            bitmask = 1 << i
            if h & bitmask:
                v[i] += 1   # ビットが立ってたら +1
            else:
                v[i] -= 1   # 立ってなければ -1
    # 最終ビット列を構築
    fingerprint = 0
    for i in range(hashbits):
        if v[i] >= 0:
            fingerprint |= 1 << i
    return fingerprint

def hamming_distance(x, y):
    return bin(x ^ y).count("1")

doc1 = "the cat sat on the mat"
doc2 = "the cat sat on a mat"
doc3 = "completely different sentence"

h1 = simhash(doc1.split())
h2 = simhash(doc2.split())
h3 = simhash(doc3.split())

print("hamming(doc1, doc2):", hamming_distance(h1, h2))
print("hamming(doc1, doc3):", hamming_distance(h1, h3))