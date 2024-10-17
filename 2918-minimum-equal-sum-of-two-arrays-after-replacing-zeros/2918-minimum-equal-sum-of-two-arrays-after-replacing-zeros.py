class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        flex1 = 0
        sum1 = 0
        for num in nums1:
            if num == 0:
                flex1 += 1
                sum1 += 1
            else:
                sum1 += num
              
        sum2 = 0
        flex2 = 0
        for num in nums2:
            if num == 0:
                flex2 += 1
                sum2 += 1
            else:
                sum2 += num
                
        if sum1 == sum2:
            return sum1

        if (sum1 > sum2 and not flex2) or (sum1 < sum2 and not flex1):
            return -1
        
        return max(sum1, sum2)