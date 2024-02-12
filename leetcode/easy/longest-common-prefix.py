class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        n = len(strs)
        if n < 1:
            return 0
        if n == 1:
            return strs[0]

        min_len = min(map(lambda x: len(x), strs))
        for i in range(min_len):
            c = strs[0][i]
            for j in range(1, n):
                if strs[j][i] != c:
                    return ans
            ans += c

        return ans
