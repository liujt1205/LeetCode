class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i, j = 0, 0
        while i < len(str1):
            if 0 <= ord(str2[j]) - ord(str1[i]) <= 1 or ord(str1[i]) - ord(str2[j]) == 25:
                j += 1
                if j == len(str2):
                    return True
            i += 1
        return False