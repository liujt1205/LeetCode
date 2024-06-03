class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        pos_s = 0
        pos_t = 0
        while pos_s < len(s) and pos_t < len(t):
            if s[pos_s] == t[pos_t]:
                pos_t += 1
            pos_s += 1
        return len(t) - pos_t
                