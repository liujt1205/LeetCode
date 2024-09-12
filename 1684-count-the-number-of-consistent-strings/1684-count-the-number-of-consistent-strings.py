class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        charSet = set(allowed)
        res = 0
        for word in words:
            if set(word).issubset(charSet):
                res += 1
                
        return res