class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        i = 0
        while i < len(s):
            match(s[i]):
                case "M":
                    total += 1000
                case "D":
                    total += 500
                case "C":
                    if i + 1 < len(s) and s[i + 1] in ["D", "M"]:
                        total -= 100
                    else:
                        total += 100
                case "L":
                    total += 50
                case "X":
                    if i + 1 < len(s) and s[i + 1] in ["L", "C"]:
                        total -= 10
                    else:
                        total += 10
                case "V":
                    total += 5
                case "I":
                    if i + 1 < len(s) and s[i + 1] in ["V", "X"]:
                        total -= 1
                    else:
                        total += 1
            i += 1

        return total
