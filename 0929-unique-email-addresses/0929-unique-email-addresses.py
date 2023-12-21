class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        memo = set()
        for email in emails:
            l = email.split('@')
            ln = l[0]
            ln = self.clean(ln)
            key = ln + '@' + l[1]
            memo.add(key)
        return len(memo)
    
    def clean(self, ln):
        res = ln.split('+')[0]
        res = ''.join(res.split('.'))
        return res