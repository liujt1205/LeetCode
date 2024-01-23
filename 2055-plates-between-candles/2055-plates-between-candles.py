class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        left = [-1] * len(s)
        right = [-1] * len(s)
        plate = [0] * len(s)
        if s[0] == '|':
            plate[0] = 1
        else:
            left[0] = 0
        min = -1
        count = 0
        for i in range(0, len(s)):
            if s[i] == '|':
                min = i
            else:
                count += 1
            plate[i] = count
            left[i] = min
        if s[-1] == '*':
            right[-1] = len(s) - 1
        min = -1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '|':
                min = i
            right[i] = min
        idx = 0
        res = [0] * len(queries)
        for start, end in queries:
            left_candle = right[start]
            right_candle = left[end]
            if right_candle <= left_candle or right_candle == -1 or left_candle == -1:
                res[idx] = 0
            else:
                res[idx] = plate[right_candle] - plate[left_candle]
            idx += 1
        return res