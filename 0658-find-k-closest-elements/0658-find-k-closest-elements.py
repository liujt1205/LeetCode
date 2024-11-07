class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] > x:
                right = mid - 1
            else:
                left = mid + 1
        
        if right == -1:
            return arr[:k]
        
        if right == len(arr) - 1:
            return arr[len(arr) - k:]
        
        left = right
        while left >= 0 and right < len(arr) and right - left + 1 < k:
            if left == 0 or (right < len(arr) - 1 and abs(arr[left - 1] - x) > abs(arr[right + 1] - x)):
                right += 1
            else:
                left -= 1
                
        if left > 0 and abs(arr[left - 1] - x) < abs(arr[right] - x):
            left -= 1
            right -= 1
        elif right < len(arr) - 1 and abs(arr[left] - x) > abs(arr[right + 1] - x):
            left += 1
            right += 1
            
        return arr[left: right + 1]