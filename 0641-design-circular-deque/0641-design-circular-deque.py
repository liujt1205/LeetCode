class MyCircularDeque:

    def __init__(self, k: int):
        self.max_size = k
        self.head = Node(-1)
        self.head.prev = self.head
        self.head.next = self.head
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.size == self.max_size:
            return False
        newNode = Node(value)
        newNode.next = self.head.next
        newNode.prev = self.head
        self.head.next.prev = newNode
        self.head.next = newNode
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size == self.max_size:
            return False
        newNode = Node(value)
        newNode.next = self.head
        newNode.prev = self.head.prev
        self.head.prev.next = newNode
        self.head.prev = newNode
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.size == 0:
            return False
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.size == 0:
            return False
        self.head.prev.prev.next = self.head
        self.head.prev = self.head.prev.prev
        self.size -= 1
        return True

    def getFront(self) -> int:
        return self.head.next.val

    def getRear(self) -> int:
        return self.head.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size
    
class Node:
    def __init__(self, value):
        self.val = value
        self.prev = None
        self.next = None
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()