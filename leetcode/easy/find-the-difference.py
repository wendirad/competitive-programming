class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        n = len(s)

        if n < 1:
            return t

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        for i, c in enumerate(sorted_t):
            if i < n and c != sorted_s[i]:
                return c

        return sorted_t[-1]
