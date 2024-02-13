class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def check(string):
            start, end = 0, len(string) - 1
            while start < end:
                if string[start] != string[end]:
                    return False
                start += 1
                end -= 1
            return True
        for word in words:
            if check(word):
                return word
        return ""