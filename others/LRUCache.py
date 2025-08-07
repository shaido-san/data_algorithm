from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1  
        self.cache.move_to_end(key)  
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)  
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  

lru = LRUCache(3)

lru.put("A", 100)
lru.put("B", 200)
lru.put("C", 300)

print(lru.get("A"))  

lru.put("D", 400) 

print(lru.cache) 