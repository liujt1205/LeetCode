class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count = Counter()
        minimum = float('inf')
        for num in basket1:
            count[num] += 1
            if num < minimum:
                minimum = num

        for num in basket2:
            count[num] -= 1
            if num < minimum:
                minimum = num

        total = 0
        for key in count:
            if count[key] % 2 != 0:
                return -1
            total += abs(count[key]) // 2

        sortedKey = sorted(count.keys())
        res = 0
        i = 0
        while total > 0:
            swap = min(total, abs(count[sortedKey[i]]))
            res += min(sortedKey[i], minimum * 2) * swap // 2
            total -= swap
            i += 1

        return res