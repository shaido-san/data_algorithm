import hashlib

class BloomFilter:
    def __init__(self, size=100, hash_count=3):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size

    def _hashes(self, item):
        for i in range(self.hash_count):
            digest = hashlib.md5((str(i) + item).encode()).hexdigest()
            yield int(digest, 16) % self.size

    def add(self, item):
        for h in self._hashes(item):
            self.bit_array[h] = 1

    def __contains__(self, item):
        return all(self.bit_array[h] for h in self._hashes(item))

bf = BloomFilter(size=20, hash_count=3)
bf.add("cat")
bf.add("dog")

print("cat" in bf)   
print("dog" in bf)   
print("bird" in bf)  