class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0

        indexr = [0] * (n1 + 1)  # index of s2 matched at start of each s1 block
        countr = [0] * (n1 + 1)  # number of s2 repeats found till each s1 block

        index = 0  # index in s2
        count = 0  # number of s2 matches

        for i in range(1, n1 + 1):
            for ch in s1:
                if ch == s2[index]:
                    index += 1
                if index == len(s2):
                    index = 0
                    count += 1

            countr[i] = count
            indexr[i] = index

            # try to find a cycle
            for k in range(i):
                if indexr[k] == index:
                    # cycle found between k and i
                    prev_count = countr[k]
                    pattern_count = ((n1 - k) // (i - k)) * (countr[i] - countr[k])
                    remain_count = countr[k + (n1 - k) % (i - k)] - countr[k]
                    return (prev_count + pattern_count + remain_count) // n2

        return countr[n1] // n2