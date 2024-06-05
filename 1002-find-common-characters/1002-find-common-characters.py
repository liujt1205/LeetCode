class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freq = [float('inf')] * 26
        for word in words:
            temp = [0] * 26
            for char in word:
                temp[ord(char) - ord('a')] += 1
            for i in range(26):
                freq[i] = min(freq[i], temp[i])
        res = []
        for i in range(26):
            for _ in range(freq[i]):
                res.append(chr(i + ord('a')))
        return res