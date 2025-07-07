class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.key2val = {}
        self.key2freq = {}
        self.freq2key = defaultdict(OrderedDict)
        self.minFreq = 0

    def get(self, key: int) -> int:
        if key not in self.key2val:
            return -1
        
        preFreq = self.key2freq[key]
        self.key2freq[key] = preFreq + 1
        self.freq2key[preFreq].pop(key)
        if not self.freq2key[preFreq]:
            del self.freq2key[preFreq]
        self.freq2key[preFreq + 1][key] = 1
        if self.minFreq not in self.freq2key:
            self.minFreq += 1
        
        return self.key2val[key]

    def put(self, key: int, value: int) -> None:
        if self.cap <= 0:
            return

        if key in self.key2val:
            self.get(key)
            self.key2val[key] = value
            return

        if len(self.key2val) == self.cap:
            key2del, _ = self.freq2key[self.minFreq].popitem(last = False)
            del self.key2val[key2del]
            del self.key2freq[key2del]

        self.key2val[key] = value
        self.key2freq[key] = 1
        self.freq2key[1][key] = 1
        self.minFreq = 1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)