class MyHashSet:

    def __init__(self):
        self.memo = [[] for _ in range(100)]

    def add(self, key: int) -> None:
        index = key % 100
        if key not in self.memo[index]:
            self.memo[index].append(key)

    def remove(self, key: int) -> None:
        index = key % 100
        if key in self.memo[index]:
            self.memo[index].remove(key)

    def contains(self, key: int) -> bool:
        index = key % 100
        return key in self.memo[index]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)