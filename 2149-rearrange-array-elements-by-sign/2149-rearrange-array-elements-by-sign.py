class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = []
        pos = deque()
        neg = deque()
        for num in nums:
            if num > 0:
                if neg:
                    res.append(num)
                    res.append(neg.popleft())
                else:
                    pos.append(num)
            else:
                if pos:
                    res.append(pos.popleft())
                    res.append(num)
                else:
                    neg.append(num)
        return res