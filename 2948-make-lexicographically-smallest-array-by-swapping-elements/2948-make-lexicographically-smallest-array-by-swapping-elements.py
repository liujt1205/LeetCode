class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sorted_nums = sorted(nums)
        group_id = 0
        groups = []
        cur_group = deque()
        cur_group.append(sorted_nums[0])
        num_to_group = {}
        num_to_group[sorted_nums[0]] = group_id
        for i in range(1, len(nums)):
            if sorted_nums[i] - sorted_nums[i - 1] > limit:
                groups.append(cur_group)
                group_id += 1
                cur_group = deque()
            cur_group.append(sorted_nums[i])
            num_to_group[sorted_nums[i]] = group_id
        groups.append(cur_group)

        res = []
        for num in nums:
            group_id = num_to_group[num]
            value = groups[group_id].popleft()
            res.append(value)

        return res
