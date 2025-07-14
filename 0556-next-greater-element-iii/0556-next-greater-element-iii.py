class Solution:
    def nextGreaterElement(self, n: int) -> int:
        seen = []
        while n > 0:
            last = n % 10
            n = n // 10
            if not seen or last >= seen[-1]:
                seen.append(last)
            else:
                nextLarger = bisect_right(seen, last)
                temp = seen[nextLarger]
                seen[nextLarger] = last
                n = n * 10 + temp
                for digit in seen:
                    n = n * 10 + digit
                if n >= 2 ** 31:
                    return -1
                return n

        return -1