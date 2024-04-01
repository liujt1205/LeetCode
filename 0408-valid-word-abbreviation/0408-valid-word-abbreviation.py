class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        while i < len(abbr) and j < len(word):
            if abbr[i].isdigit():
                cur = int(abbr[i])
                if cur == 0:
                    return False
                i += 1
                while i < len(abbr) and abbr[i].isdigit():
                    cur = cur * 10 + int(abbr[i])
                    i += 1
                j += cur
            else:
                if abbr[i] == word[j]:
                    i += 1
                    j += 1
                else:
                    return False
        return i == len(abbr) and j == len(word)