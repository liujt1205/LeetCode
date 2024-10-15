class FirstUnique:

    def __init__(self, nums: List[int]):
        self.count = {}
        self.queue = deque()
        
        for num in nums:
            if num not in self.count:
                self.count[num] = 1
                self.queue.append(num)
            else:
                self.count[num] += 1
                
        while self.queue and self.count[self.queue[0]] != 1:
            self.queue.popleft()        

    def showFirstUnique(self) -> int:
        return self.queue[0] if self.queue else -1

    def add(self, value: int) -> None:
        if value not in self.count:
            self.count[value] = 1
            self.queue.append(value)
        else:
            self.count[value] += 1
            
        while self.queue and self.count[self.queue[0]] != 1:
            self.queue.popleft()


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)