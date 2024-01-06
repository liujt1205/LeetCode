class MyHashMap:

    def __init__(self):
        self.memo = [[] for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        index = key % 1000
        ins_index = 0
        while ins_index < len(self.memo[index]):
            if self.memo[index][ins_index][0] == key:
                self.memo[index][ins_index] = (key, value)
                break
            ins_index += 1
        if ins_index == len(self.memo[index]):
            self.memo[index].append((key, value))
        
            
    def get(self, key: int) -> int:
        index = key % 1000
        for i in range(len(self.memo[index])):
            if self.memo[index][i][0] == key:
                return self.memo[index][i][1]
        return -1

    def remove(self, key: int) -> None:
        index = key % 1000
        for i in range(len(self.memo[index])):
            if self.memo[index][i][0] == key:
                del self.memo[index][i]
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)