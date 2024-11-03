class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = []
        for char in s:
            if char.isalpha():
                clean.append(char.lower())
            elif char.isdigit():
                clean.append(char)
        
        for i in range(len(clean)):
            if i >= len(clean) - i:
                break
            if clean[i] != clean[len(clean) - i - 1]:
                return False
            
        return True