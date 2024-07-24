class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped = {}
        for num in nums:
            mapped_char = ""
            cur = num
            if cur == 0:
               mapped_char = str(mapping[0]) + mapped_char
            else:
                while cur > 0:
                    last_digit = cur % 10
                    mapped_char = str(mapping[last_digit]) + mapped_char
                    cur = cur // 10
            mapped_num = int(mapped_char)
            str_num_array = mapped.get(str(mapped_num), [])
            str_num_array.append(num)
            mapped[str(mapped_num)] = str_num_array
        res = []
        for key in sorted(mapped.keys(), key=lambda x: int(x)):
            res.extend(mapped[key])
        return res