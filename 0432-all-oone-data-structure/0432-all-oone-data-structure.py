class AllOne:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.map = {}
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        if key not in self.map:
            firstNode = self.head.next
            if firstNode == self.tail or firstNode.freq != 1:
                newNode = Node(1)
                newNode.keys.add(key)
                newNode.prev = self.head
                newNode.next = firstNode
                self.head.next = newNode
                firstNode.prev = newNode
                self.map[key] = newNode
            else:
                firstNode.keys.add(key)
                self.map[key] = firstNode
        else:
            curNode = self.map[key]
            curNode.keys.remove(key)
            curFreq = curNode.freq
            if curNode.next == self.tail or curNode.next.freq != curFreq + 1:
                newNode = Node(curFreq + 1)
                newNode.keys.add(key)
                newNode.prev = curNode
                newNode.next = curNode.next
                curNode.next.prev = newNode
                curNode.next = newNode
                self.map[key] = newNode
            else:
                curNode.next.keys.add(key)
                self.map[key] = curNode.next
            if not curNode.keys:
                self.removeNode(curNode)
        

    def dec(self, key: str) -> None:
        curNode = self.map[key]
        curNode.keys.remove(key)
        curFreq = curNode.freq
        if curFreq == 1:
            del self.map[key]
        else:
            if curNode.prev == self.head or curNode.prev.freq != curFreq - 1:
                newNode = Node(curFreq - 1)
                newNode.keys.add(key)
                newNode.prev = curNode.prev
                newNode.next = curNode
                curNode.prev.next = newNode
                curNode.prev = newNode
                self.map[key] = newNode
            else:
                curNode.prev.keys.add(key)
                self.map[key] = curNode.prev
        if not curNode.keys:
            self.removeNode(curNode)
        

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
class Node:
    def __init__(self, freq):
        self.freq = freq
        self.prev = None
        self.next = None
        self.keys = set()

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()