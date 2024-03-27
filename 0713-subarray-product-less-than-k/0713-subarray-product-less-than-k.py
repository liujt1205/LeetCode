class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        products = [1] * (len(nums) + 1)
        cur = 1
        res = 0
        for i in range(len(nums)):
            cur *= nums[i]
            products[i + 1] *= cur
        
        def find(products, limit, i):
            start = i + 1
            end = len(products) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if products[mid] <= limit:
                    start = mid + 1
                else:
                    end = mid - 1
            return start - 1
        
        for i in range(len(nums)):
            limit = products[i] * (k - 1)
            res += find(products, limit, i) - i
            
        return res