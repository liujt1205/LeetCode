class FreqStack:

    def __init__(self):
        self.count = collections.defaultdict(list)
        self.freq = collections.defaultdict(int)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        newFreq = self.freq[val] + 1
        self.freq[val] = newFreq
        if newFreq > self.maxFreq:
            self.maxFreq = newFreq
        self.count[newFreq].append(val)

    def pop(self) -> int:
        res = self.count[self.maxFreq].pop()
        self.freq[res] -= 1
        if not self.count[self.maxFreq]:
            self.maxFreq -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()