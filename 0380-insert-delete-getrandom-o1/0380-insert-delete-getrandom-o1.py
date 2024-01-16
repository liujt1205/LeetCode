class RandomizedSet:

    def __init__(self):
        self._list = []
        self._dict = {}

    def insert(self, val: int) -> bool:
        if val not in self._dict:
            self._list.append(val)
            self._dict[val] = len(self._list) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self._dict:
            index = self._dict[val]
            self._list[index] = self._list[-1]
            self._dict[self._list[-1]] = index
            self._list.pop()
            del self._dict[val]
            return True
        return False

    def getRandom(self) -> int:
        return choice(self._list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()