class Solution:
    def removeVowels(self, s: str) -> str:
        res = []
        vowels = 'aeiou'
        for char in s:
            if char not in vowels:
                res.append(char)
                
        return ''.join(res)