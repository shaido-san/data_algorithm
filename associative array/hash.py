from string import ascii_letters

def hash_func(text):
    hash_num = 0
    for c in text:
        hash_num += ascii_letters.index(c)
    return hash_num

hash_val = hash_func("abc")
print(hash_val)