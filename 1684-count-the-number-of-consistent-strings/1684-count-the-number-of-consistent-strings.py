class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        for word in words:
            if set(word).issubset(set(allowed)):
                res += 1
                
        return res