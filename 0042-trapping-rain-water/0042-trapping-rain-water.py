class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left = 0
        right = len(height) - 1
        cur_left = 0
        cur_right = 0
        while left != right:
            cur_left = max(cur_left, height[left])
            cur_right = max(cur_right, height[right])
            if cur_left > cur_right:
                res += cur_right - height[right]
                right -= 1
            else:
                res += cur_left - height[left]
                left += 1
        return res