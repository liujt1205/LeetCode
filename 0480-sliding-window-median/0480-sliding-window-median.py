class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = SortedList(nums[:k])
        medians = []

        for i in range(k, len(nums) + 1):
            # Compute the median
            if k % 2 == 1:
                medians.append(float(window[k // 2]))
            else:
                medians.append((window[k // 2 - 1] + window[k // 2]) / 2)

            if i == len(nums):
                break

            # Remove the outgoing element
            window.remove(nums[i - k])
            # Insert the incoming element
            window.add(nums[i])

        return medians