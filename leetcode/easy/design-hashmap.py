class MyHashMap:

    def __init__(self):
        self.keys = []
        self.values = []

    def put(self, key: int, value: int) -> None:
        for idx, val in enumerate(self.keys):
            if val == key:
                self.values[idx] = value
                return
            
        self.keys.append(key)
        self.values.append(value)

    def get(self, key: int) -> int:
        for idx, val in enumerate(self.keys):
            if val == key:
                return self.values[idx]
        return -1

    def remove(self, key: int) -> None:
        for idx, val in enumerate(self.keys):
            if val == key:
                self.keys.pop(idx)
                self.values.pop(idx)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)