class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            return self.gcdOfStrings(str2, str1)
        
        if str1 == str2:
            return str1
        elif str1 == str2[:len(str1)]:
            return self.gcdOfStrings(str1, str2[len(str1):])
        else:
            return ""