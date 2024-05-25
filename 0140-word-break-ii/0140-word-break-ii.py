class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = [set() for _ in range(11)]
        for word in wordDict:
            wordSet[len(word)].add(word)

        memo = [[] for _ in range(len(s) + 1)]
        for i in range(len(s)):
            for j in range(min(10, i + 1)):
                if s[i - j:i + 1] in wordSet[j + 1]:
                    if len(memo[i - j]) == 0 and i == j:
                        memo[i + 1].append(s[:i + 1])
                    else:
                        for string in memo[i - j]:
                            temp = string + ' ' + s[i - j: i + 1]
                            memo[i + 1].append(temp)
        return memo[len(s)]