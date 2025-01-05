class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shift = [0] * len(s)
        for start, end, direct in shifts:
            change = 1 if direct == 1 else -1
            shift[start] += change
            if end < len(s) - 1:
                shift[end + 1] -= change

        for i in range(1, len(s)):
            shift[i] += shift[i - 1]

        res = []
        for i in range(len(s)):
            index = (26 + ord(s[i]) - ord('a') + shift[i]) % 26
            res.append(chr(ord('a') + index))

        return ''.join(res)