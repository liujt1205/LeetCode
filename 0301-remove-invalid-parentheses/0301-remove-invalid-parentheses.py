class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        r_right = 0
        count = 0
        for char in s:
            if char not in "()":
                continue
            if char == '(':
                count += 1
            elif count == 0:
                r_right += 1
            else:
                count -= 1
                
        r_left = count
        min_r = r_left + r_right
        res = []
        
        def helper(cur_string, index, left, right, count):
            if index == len(s):
                if count == 0:
                    res.append("".join(cur_string))
                return
            if s[index] not in "()":
                cur_string.append(s[index])
                helper(cur_string, index + 1, left, right, count)
                cur_string.pop()
                return
            if s[index] == '(':
                cur_string.append('(')
                helper(cur_string, index + 1, left, right, count + 1)
                cur_string.pop()
                helper(cur_string, index + 1, left + 1, right, count)
            else:
                if count > 0:
                    cur_string.append(')')
                    helper(cur_string, index + 1, left, right, count - 1)
                    cur_string.pop()
                if right < r_right:
                    helper(cur_string, index + 1, left, right + 1, count)
                    
        helper([], 0, 0, 0, 0)
        return list(set(res))