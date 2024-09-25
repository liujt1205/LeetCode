# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        for i, list_head in enumerate(lists):
            if list_head:
                pq.append((list_head.val, i, list_head))
        heapq.heapify(pq)
        newHead = ListNode(-1)
        cur = newHead
        while pq:
            nextVal, index, nextNode = heapq.heappop(pq)
            cur.next = nextNode
            if nextNode.next:
                heapq.heappush(pq, (nextNode.next.val, index, nextNode.next))
            nextNode.next = None
            cur = nextNode
            
        return newHead.next