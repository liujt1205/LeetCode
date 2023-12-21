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
        res = ln.split('+')[0]
        res = ''.join(res.split('.'))
        return res