# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        fakeHead = PolyNode(0, 0)
        cur = fakeHead
        while poly1 and poly2:
            if poly1.power == poly2.power:
                newCoeff = poly1.coefficient + poly2.coefficient
                if newCoeff != 0:
                    cur.next = PolyNode(newCoeff, poly1.power)
                    cur = cur.next
                poly1 = poly1.next
                poly2 = poly2.next
            elif poly1.power > poly2.power:
                cur.next = PolyNode(poly1.coefficient, poly1.power)
                cur = cur.next
                poly1 = poly1.next
            else:
                cur.next = PolyNode(poly2.coefficient, poly2.power)
                cur = cur.next
                poly2 = poly2.next
        if not poly1:
            cur.next = poly2
        elif not poly2:
            cur.next = poly1
        return fakeHead.next
        