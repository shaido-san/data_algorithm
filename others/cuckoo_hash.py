import random

class CuckooHashTable:
    def __init__(self, size=11):
        self.size = size
        self.table = [None] * size
        self.max_loop = size  

    def _hash1(self, key):
        return hash(key) % self.size

    def _hash2(self, key):
        return (hash(key) // self.size) % self.size

    def insert(self, key):
        pos = self._hash1(key)
        for _ in range(self.max_loop):
            if self.table[pos] is None:
                self.table[pos] = key
                return
            
            key, self.table[pos] = self.table[pos], key
    
            if pos == self._hash1(key):
                pos = self._hash2(key)
            else:
                pos = self._hash1(key)
       
        self._rehash()
        self.insert(key)

    def search(self, key):
        return self.table[self._hash1(key)] == key or \
               self.table[self._hash2(key)] == key

    def _rehash(self):
        print("Rehashing...")
        old = [k for k in self.table if k is not None]
        self.size *= 2
        self.table = [None] * self.size
        for k in old:
            self.insert(k)

ht = CuckooHashTable()
for k in ["apple", "banana", "cherry", "date", "elderberry"]:
    ht.insert(k)

print("Search apple:", ht.search("apple"))
print("Search mango:", ht.search("mango"))
print("Table:", ht.table)