class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        bigger = deque()
        smaller = deque()
        last = -1
        res = 0
        for i in range(len(nums)):
            cur = nums[i]
            while bigger and nums[bigger[-1]] < cur:
                bigger.pop()
                
            bigger.append(i)
            
            while smaller and nums[smaller[-1]] > cur:
                smaller.pop()
                
            smaller.append(i)
            
            while smaller and bigger and nums[bigger[0]] - nums[smaller[0]] > 2:
                if bigger[0] > smaller[0]:
                    last = smaller.popleft()
                else:
                    last = bigger.popleft()
                    
            res += i - last
            
        return res
                
            
        