from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)  # 最近使ったので最後に移動
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # 一番古いの捨てる

cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  
cache.put(3, 3)      
print(cache.get(2))  