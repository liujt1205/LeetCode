class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for char in s:
            if char in "BD" and stack and ord(char) - ord(stack[-1]) == 1:
                stack.pop()
            else:
                stack.append(char)
                
        return len(stack)
                
            
                
                