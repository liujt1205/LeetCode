class RandomizedCollection:

    def __init__(self):
        self.indexes = {}
        self.items = []
        

    def insert(self, val: int) -> bool:
        if val not in self.indexes:
            self.indexes[val] = set()
        self.indexes[val].add(len(self.items))
        self.items.append(val)
        return len(self.indexes[val]) == 1

    def remove(self, val: int) -> bool:
        if val not in self.indexes or not self.indexes[val]:
            return False
        index = self.indexes[val].pop()
        last_val = self.items[-1]
        self.indexes[last_val].add(index)
        self.indexes[last_val].discard(len(self.items) - 1)

        self.items[index] = last_val
        self.items.pop()
        if not self.indexes[val]:
            del self.indexes[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.items)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()