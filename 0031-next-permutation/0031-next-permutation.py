class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def findNextBigger(nums, start, target):
            end = len(nums) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] <= target:
                    end = mid - 1
                else:
                    start = mid + 1
            
            return start - 1
        
        def reverseList(nums, start):
            i = 0
            while start + i < len(nums) - i:
                nums[start + i], nums[len(nums) - 1 - i] = nums[len(nums) - 1 - i], nums[start + i]
                i += 1
        
        i = len(nums) - 1
        while i > 0:
            if nums[i - 1] < nums[i]:
                index = findNextBigger(nums, i, nums[i - 1])
                nums[i - 1], nums[index] = nums[index], nums[i - 1]
                break
            i -= 1

        reverseList(nums, i)
        
            