class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        res = float('inf')
        left, right = 0, 0
        bit_count = [0] * 32
        def convertBits(bit_count):
            res = 0
            for i in range(32):
                if bit_count[i]:
                    res |= (1 << i)
                    
            return res
        
        while right < len(nums):
            for i in range(32):
                if nums[right] & (1 << i):
                    bit_count[i] += 1
                    if bit_count[i] == 0:
                        count -= 1
            
            while left <= right and convertBits(bit_count) >= k:
                res = min(res, right - left + 1)
                for i in range(32):
                    if nums[left] & (1 << i):
                        bit_count[i] -= 1
                left += 1
            
            right += 1
                
        return res if res != float('inf') else -1
            