class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        counts = defaultdict(int)
        distinct = 0
        for digit in digits:
            if counts[digit] == 0:
                distinct += 1
            counts[digit] += 1

        res = 0
        for start in counts:
            if start == 0:
                continue
            counts[start] -= 1
            for mid in counts:
                if counts[mid] == 0:
                    continue
                counts[mid] -= 1
                for end in counts:
                    if counts[end] == 0 or end % 2 != 0:
                        continue
                    res += 1
                counts[mid] += 1
            counts[start] += 1

        return res