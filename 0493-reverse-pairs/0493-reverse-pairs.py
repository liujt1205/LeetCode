class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(start, end):
            if start >= end:
                return 0
            
            mid = (start + end) // 2
            count = mergeSort(start, mid) + mergeSort(mid + 1, end)
            j = mid + 1
            for i in range(start, mid + 1):
                while j <= end and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)

            i = start
            j = mid + 1
            sorted_section = []
            while i <= mid and j <= end:
                if nums[i] < nums[j]:
                    sorted_section.append(nums[i])
                    i += 1
                else:
                    sorted_section.append(nums[j])
                    j += 1

            sorted_section.extend(nums[j: end + 1])
            sorted_section.extend(nums[i: mid + 1])
            nums[start: end + 1] = sorted_section

            return count

        return mergeSort(0, len(nums) - 1)