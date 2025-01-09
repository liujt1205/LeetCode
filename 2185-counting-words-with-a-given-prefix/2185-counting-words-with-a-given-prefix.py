class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        n = len(pref)
        for word in words:
            if word.startswith(pref):
                res += 1

        return res