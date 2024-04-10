class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        index = 0
        
        def helper(left, right):
            nonlocal index
            if index == len(preorder):
                return True
            cur = preorder[index]
            if cur >= right or cur <= left:
                return False
            index += 1
            leftSide = helper(left, cur) 
            rightSide = helper(cur, right)
            return leftSide or rightSide
            
        return helper(-float('inf'), float('inf'))