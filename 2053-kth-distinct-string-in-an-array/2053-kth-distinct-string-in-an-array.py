class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        memo = {}
        for string in arr:
            if string in memo:
                memo[string] = False
            else:
                memo[string] = True
        
        for string in arr:
            if memo[string] == True:
                k -= 1
            if k == 0:
                return string
        return ""