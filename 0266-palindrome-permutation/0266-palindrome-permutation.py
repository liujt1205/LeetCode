class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = Counter(s)
        findOdd = 0
        for char in count:
            if count[char] % 2 != 0:
                findOdd += 1
            if findOdd > 1:
                return False
            
        return True