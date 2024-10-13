class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        occurrences = {}
        count = [0] * 26
        uniqueChar = 0
        left = 0
        for right in range(len(s)):
            if count[ord(s[right]) - ord('a')] == 0:
                uniqueChar += 1
            count[ord(s[right]) - ord('a')] += 1
            while left <= right and right - left + 1 > maxSize or uniqueChar > maxLetters:
                count[ord(s[left]) - ord('a')] -= 1
                if count[ord(s[left]) - ord('a')] == 0:
                    uniqueChar -= 1
                left += 1
            for i in range(right - left + 2 - minSize):
                substring = s[left + i: right + 1]
                if substring not in occurrences:
                    occurrences[substring] = 0
                occurrences[substring] += 1
            
        return max(occurrences.values()) if occurrences.values() else 0