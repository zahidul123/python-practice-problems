### Problem-3: Implement an LRU Cache (Least Recently Used)
#Simulate caching in a backend system. You need to implement a cache with `get()` and `put()` methods.
    
#-   **Hint**: Use `OrderedDict` or create a custom class with a doubly linked list.

from collections import OrderedDict as OD
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OD()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
# Example usage:
lru_cache = LRUCache(2)
lru_cache.put(1, 1)  # cache is {1=1}
lru_cache.put(2, 2)  # cache is {1=1, 2=2}
print(lru_cache.get(1))    # return 1
lru_cache.put(3, 3)  # evicts key 2, cache is {1=1, 3=3}
print(lru_cache.get(2))    # return -1 (not found)
lru_cache.put(4, 4)  # evicts key 1, cache is {4=4, 3=3}



