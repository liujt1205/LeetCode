class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        charSet = set(allowed)
        res = 0
        for word in words:
            wordSet = set(word)
            if wordSet.issubset(charSet):
                res += 1
                
        return res