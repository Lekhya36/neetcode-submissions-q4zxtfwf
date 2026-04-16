class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.map = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key, value):
        idx = self._hash(key)
        bucket = self.map[idx]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # update
                return

        bucket.append((key, value))  # insert

    def get(self, key):
        idx = self._hash(key)
        bucket = self.map[idx]

        for k, v in bucket:
            if k == key:
                return v

        return -1

    def remove(self, key):
        idx = self._hash(key)
        bucket = self.map[idx]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return      


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)