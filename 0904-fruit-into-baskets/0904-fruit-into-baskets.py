class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        distinct = 0
        count = Counter()
        left = 0
        res = 0
        for i in range(len(fruits)):
            cur = fruits[i]
            if count[cur] == 0:
                distinct += 1
            count[cur] += 1
            while distinct > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    distinct -= 1
                left += 1
            res = max(res, i - left + 1)

        return res