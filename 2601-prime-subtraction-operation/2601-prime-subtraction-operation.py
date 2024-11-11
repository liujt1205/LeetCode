class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                continue
            prime = self.findNextPrime(nums[i] + 1 - nums[i + 1], nums[i])
            if prime < 1:
                return False
            else:
                nums[i] -= prime
                
        return True
    
    def findNextPrime(self, diff, num):
        if diff >= num:
            return -1
        for i in range(max(diff, 2), num):
            if self.isPrime(i):
                return i
            
        return -1
    
    def isPrime(self, num):
        for i in range(2, min(round(sqrt(num)) + 1, num)):
            if num % i == 0:
                return False
            
        return True