class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        temp = [0] * len(nums)
        def merge(left, mid, right):
            for i in range(left, mid + 1):
                temp[i] = nums[i]
            for i in range(mid + 1, right + 1):
                temp[i] = nums[i]
            l1 = mid + 1 - left
            l2 = right - mid
            i, j, k = 0, 0, left
            while i < l1 and j < l2:
                if temp[left + i] <= temp[mid + 1 + j]:
                    nums[k] = temp[left + i]
                    i += 1
                else:
                    nums[k] = temp[mid + 1 + j]
                    j += 1
                k += 1
            while i < l1:
                nums[k] = temp[left + i]
                i += 1
                k += 1
            while j < l2:
                nums[k] = temp[mid + 1 + j]
                j += 1
                k += 1
                
        def merge_sort(left, right):
            if left >= right:
                return 
            mid = (left + right) // 2
            merge_sort(left, mid)
            merge_sort(mid + 1, right)
            merge(left, mid, right)
        
        merge_sort(0, len(nums) - 1)
        return nums