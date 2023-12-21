class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        memo = {}
        res = 0
        for email in emails:
            l = email.split('@')
            ln = l[0]
            ln = self.clean(ln)
            key = ln + '@' + l[1]
            if memo.get(key, True):
                res += 1
                memo[key] = False
        return res
    
    def clean(self, ln):
        res = ''
        for c in ln:
            if c == '.':
                continue
            elif c == '+':
                break
            else:
                res += c
        return res