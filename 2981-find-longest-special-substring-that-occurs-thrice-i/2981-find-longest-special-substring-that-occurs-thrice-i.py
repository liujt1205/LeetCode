class Solution:
    def maximumLength(self, s: str) -> int:
        ans = -1
        n = len(s)
        counter = 1
        prev = '#'
        # Initialize a 2D list for 26 letters and n + 2 lengths
        p = [[0] * (n + 2) for _ in range(26)]

        # First pass: build the `p` table
        for i in range(n):
            if i == 0 or s[i] != prev:
                counter = 1
            else:
                counter += 1

            char_index = ord(s[i]) - ord('a')
            p[char_index][1] += 1
            p[char_index][counter + 1] -= 1
            prev = s[i]

        # Second pass: calculate the maximum length
        for c in range(26):
            sum_runs = 0
            for length in range(1, n + 1):
                sum_runs += p[c][length]
                if sum_runs >= 3:
                    ans = max(ans, length)

        return ans