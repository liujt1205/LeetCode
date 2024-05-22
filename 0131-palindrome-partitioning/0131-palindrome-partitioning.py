class Solution:
    def partition(self, s: str) -> List[List[str]]:
        memo = defaultdict(list)
        def expand(index):
            left = index
            right = index
            nonlocal s, memo
            while left >= 0 and right < len(s) and s[left] == s[right]:
                memo[left].append(right)
                left -= 1
                right += 1

            left = index
            right = index + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                memo[left].append(right)
                left -= 1
                right += 1
                
        for index in range(len(s)):
            expand(index)
            
        res = []
        temp = []
        def help(index):
            nonlocal memo, res, temp, s
            if index == len(s):
                res.append(list(temp))
                return
            for i in memo[index]:
                temp.append(s[index:i + 1])
                help(i+1)
                temp.pop()
        
        help(0)
        return res
            