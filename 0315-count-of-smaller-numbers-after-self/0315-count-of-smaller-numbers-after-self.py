class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        copy = [[v, i] for i, v in enumerate(nums)]
        result = [0] * len(nums)
        
        def merge_sort(copy, left, right):
            if left == right:
                return
            mid = (left + right) // 2
            merge_sort(copy, left, mid)
            merge_sort(copy, mid + 1, right)
            merge(copy, left, mid, right)
            
        def merge(copy, left, mid, right):
            temp = []
            i = left
            j = mid + 1
            while i <= mid and j <= right:
                if copy[i][0] > copy[j][0]:
                    temp.append(copy[j])
                    j += 1
                else:
                    result[copy[i][1]] += j - mid - 1
                    temp.append(copy[i])
                    i += 1
            while i <= mid:
                result[copy[i][1]] += j - mid - 1
                temp.append(copy[i])
                i += 1
            while j <= right:
                temp.append(copy[j])
                j += 1
            for i in range(right - left + 1):
                copy[i + left] = temp[i]
                
            
        merge_sort(copy, 0, len(nums) - 1)
        return result