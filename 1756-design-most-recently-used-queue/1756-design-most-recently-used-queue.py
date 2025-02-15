class MRUQueue:

    def __init__(self, n: int):
        self.head = ListNode()
        self.tail = self.head
        current = self.head
        for i in range(1, n + 1):
            current.next = ListNode(i)
            current = current.next

        self.tail = current

    def fetch(self, k: int) -> int:
        current = self.head
        for _ in range(1, k):
            current = current.next

        val = current.next.val

        self.tail.next = current.next
        current.next = current.next.next
        self.tail = self.tail.next
        self.tail.next = None

        return val


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)