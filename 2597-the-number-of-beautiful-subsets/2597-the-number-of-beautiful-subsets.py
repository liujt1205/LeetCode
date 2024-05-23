class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        res = 1
        freq = defaultdict(dict)
        for num in nums:
            freq[num % k][num] = freq[num % k].get(num, 0) + 1
        for fr in freq.values():
            prev_num, curr, prev1, prev2 = -k, 1, 1, 0

            for num, freq in sorted(fr.items()):
                skip = prev1  

                if num - prev_num == k:
                    take = ((1 << freq) - 1) * prev2
                else:
                    take = ((1 << freq) - 1) * prev1

                curr = skip + take  
                prev2, prev1 = prev1, curr
                prev_num = num
            res *= curr
        return res - 1