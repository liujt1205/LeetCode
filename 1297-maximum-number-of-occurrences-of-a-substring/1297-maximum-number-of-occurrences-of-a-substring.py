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
            if right - left >= minSize:
                count[ord(s[left]) - ord('a')] -= 1
                if count[ord(s[left]) - ord('a')] == 0:
                    uniqueChar -= 1
                left += 1
            if uniqueChar <= maxLetters and right - left + 1 == minSize:
                substring = s[left: right + 1]
                if substring not in occurrences:
                    occurrences[substring] = 0
                occurrences[substring] += 1
                print(substring)
            
        return max(occurrences.values()) if occurrences.values() else 0