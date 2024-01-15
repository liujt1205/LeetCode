class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        location = [0] * 26
        for i in range(26):
            location[ord(keyboard[i]) - ord('a')] = i
        res = 0
        pre = 0
        for char in word:
            index = location[ord(char) - ord('a')]
            distance = abs(index - pre)
            res += distance
            pre = index
        return res