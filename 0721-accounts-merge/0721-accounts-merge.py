class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        memo = {}
        for account in accounts:
            username = account[0]
            if username not in memo:
                memo[username] = UnionFind()
            memo[username].add(account[1])

            for i in range(2, len(account)):
                memo[username].add(account[i])
                memo[username].union(account[i], account[i - 1])
                
        res = []
        for username in memo:
            emailLists = memo[username].generateList()
            for emailList in emailLists:
                emailList.sort()
                account = [username]
                account.extend(emailList)
                res.append(account)
                
        return res
        
class UnionFind:
    def __init__(self):
        self.indexes = {}
        self.parents = []
        self.emails = []
        self.count = 0
        
    def add(self, email):
        if email not in self.emails:
            self.parents.append(self.count)
            self.emails.append(email)
            self.indexes[email] = self.count
            self.count += 1
            
    def union(self, a, b):
        indexA = self.indexes[a]
        indexB = self.indexes[b]
        rootA = self.find(indexA)
        rootB = self.find(indexB)
        if rootA < rootB:
            self.parents[rootB] = rootA
        else:
            self.parents[rootA] = rootB
            
    def find(self, i):
        if self.parents[i] == i:
            return i
        else:
            self.parents[i] = self.find(self.parents[i])
            return self.parents[i]
        
    def generateList(self):
        lists = {}
        for i in range(self.count):
            if i == self.parents[i]:
                lists[self.emails[i]] = [self.emails[i]]
            else:
                lists[self.emails[self.find(i)]].append(self.emails[i])
        return lists.values()
            
            
            
        