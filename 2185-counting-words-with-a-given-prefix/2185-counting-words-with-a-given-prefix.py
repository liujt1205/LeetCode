class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        n = len(pref)
        for word in words:
            if len(word) >= n and word[:n] == pref:
                res += 1

        return res