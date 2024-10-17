class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        if len(nums) < 3:
            return 0
        total = 0
        neg = defaultdict(int)
        for j in range(1,len(nums)-1):
            neg[-nums[j-1] % d] += 1
            for k in range(j+1,len(nums)):
                residue = (nums[j]+nums[k]) % d 
                total += neg[residue]
        return total
            
        return res