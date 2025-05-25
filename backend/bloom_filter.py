import mmh3
from bitarray import bitarray

class BloomFilter:
    def __init__(self, size=1000, hash_count=3):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)
    
    def get_hashes(self, item):
        return [mmh3.hash(item, i) % self.size for i in range(self.hash_count)]
    
    def add(self, item):
        for hash_val in self.get_hashes(item):
            self.bit_array[hash_val] = 1
    
    def check(self, item):
        return all(self.bit_array[hash_val] for hash_val in self.get_hashes(item))

bloom = BloomFilter()

items = ["apple", "banana", "orange"]
for item in items:
    bloom.add(item)

tests = ["apple", "grape", "banana", "watermelon"]
for test in tests:
    result = bloom.check(test)
    print(f"{test}: {'いるかも' if result else 'いない'}")