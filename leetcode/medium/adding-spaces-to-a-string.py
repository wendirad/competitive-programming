class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ix = 0
        n = len(s)
        m = len(spaces)
        ans = ""

        for i in range(n):
            if ix < m and i == spaces[ix]:
                ans += " "
                ix += 1
            ans += s[i]

        return ans
