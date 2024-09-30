class CustomStack:

    def __init__(self, maxSize: int):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.maxSize = maxSize
        self.count = 0

    def push(self, x: int) -> None:
        if self.count < self.maxSize:
            newNode = Node(x)
            newNode.prev = self.head
            newNode.next = self.head.next
            self.head.next.prev = newNode
            self.head.next = newNode
            self.count += 1

    def pop(self) -> int:
        if self.count == 0:
            return -1
        target = self.head.next
        target.next.prev = self.head
        self.head.next = target.next
        self.count -= 1
        return target.val

    def increment(self, k: int, val: int) -> None:
        cur = self.tail
        while k > 0 and cur.prev != self.head:
            cur = cur.prev
            cur.val += val
            k -= 1
        
class Node:
    def __init__(self, value):
        self.val = value
        self.prev = None
        self.next = None

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)