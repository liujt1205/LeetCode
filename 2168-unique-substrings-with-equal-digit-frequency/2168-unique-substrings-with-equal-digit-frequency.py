class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        root = TrieNode()
        res = 0
        for i in range(len(s)):
            cur = root
            freq = [0] * 10
            unique = 0
            max_freq = 0
            for j in range(i, len(s)):
                cur_digit = int(s[j])
                if freq[cur_digit] == 0:
                    unique += 1
                freq[cur_digit] += 1
                max_freq = max(max_freq, freq[cur_digit])
                if not cur.children[cur_digit]:
                    cur.children[cur_digit] = TrieNode()
                cur = cur.children[cur_digit]
                if unique * max_freq == j - i + 1 and cur.visited == False:
                    res += 1
                    cur.visited = True

        return res

class TrieNode:
    def __init__(self):
        self.children = [None] * 10
        self.visited = False