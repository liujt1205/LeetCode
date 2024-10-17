class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        if len(nums) < 3:
            return 0
        reminder = [0] * d
        res = 0
        for num in nums:
            cur = num % d
            total = 0
            for i in range(d):
                target = (d * 2 - cur - i) % d
                if target == i:
                    total += reminder[i] * (reminder[i] - 1)
                else:
                    total += reminder[i] * reminder[target]
            res += total // 2
            reminder[cur] += 1
            
        return res