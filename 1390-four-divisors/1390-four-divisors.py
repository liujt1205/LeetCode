class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def checkNum(num):
            divisor = set()
            for i in range(1, int(sqrt(num)) + 1):
                if num % i == 0:
                    divisor.add(i)
                    divisor.add(num // i)
                if len(divisor) > 4:
                    return 0
            if len(divisor) == 4:
                return sum(divisor)
            else:
                return 0
        
        res = 0
        for num in nums:
            res += checkNum(num)
            
        return res
        