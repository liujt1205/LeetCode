class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        count1 = [0] * 26
        count2 = [0] * 26
        for i in range(len(word1)):
            count1[ord(word1[i]) - ord('a')] += 1
            count2[ord(word2[i]) - ord('a')] += 1
        memo = {}
        for i in range(26):
            memo[count1[i]] = memo.get(count1[i], 0) + 1
            memo[count2[i]] = memo.get(count2[i], 0) - 1
            if count1[i] == 0 and count2[i] != 0:
                return False
            if count1[i] != 0 and count2[i] == 0:
                return False
        for freq, count in memo.items():
            if count != 0:
                return False
        return True