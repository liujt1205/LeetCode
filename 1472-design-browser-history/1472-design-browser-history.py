class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = ListNode(homepage)
        
    def visit(self, url: str) -> None:
        newNode = ListNode(url)
        newNode.prev = self.cur
        self.cur.next = newNode
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        while steps and self.cur.prev:
            self.cur = self.cur.prev
            steps -= 1
            
        return self.cur.value

    def forward(self, steps: int) -> str:
        while steps and self.cur.next:
            self.cur = self.cur.next
            steps -= 1
            
        return self.cur.value
        
class ListNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)