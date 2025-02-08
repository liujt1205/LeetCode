class NumberContainers:

    def __init__(self):
        self.indexes = {}
        self.values = {}

    def change(self, index: int, number: int) -> None:
        if number not in self.indexes:
            self.indexes[number] = []
        
        self.values[index] = number
        heapq.heappush(self.indexes[number], index)

    def find(self, number: int) -> int:
        while (
            number in self.indexes 
            and len(self.indexes[number]) != 0 
            and self.values[self.indexes[number][0]] != number
        ):
            heapq.heappop(self.indexes[number])

        if number in self.indexes and len(self.indexes[number]) != 0:
            return self.indexes[number][0] 
        else:
            return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)