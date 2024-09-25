class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        memo = {}
        for cp in cpdomains:
            count, domain = cp.split(' ', 1)
            count = int(count)
            domains = domain.split('.')
            for i in range(len(domains)):
                cur = '.'.join(domains[i:])
                if cur not in memo:
                    memo[cur] = count
                else:
                    memo[cur] += count
                    
        res = []
        for key in memo:
            res.append(str(memo[key]) + " " + key)
                
        return res