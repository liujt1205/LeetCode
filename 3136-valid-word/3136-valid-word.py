class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        hasVowel = False
        hasCon = False
        for char in word:
            if char in 'aeiouAEIOU':
                hasVowel = True
            elif char in '1234567890':
                continue
            elif char.isalnum():
                hasCon = True
            else:
                return False

        return hasVowel and hasCon