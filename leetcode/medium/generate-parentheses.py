class Solution:
    o = 0
    c = 0
    ans = []
    cur = []

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        temp = []

        def recursive(op, cl):
            if op == cl == n:
                ans.append("".join(temp))
                return

            if op < n:
                temp.append("(")
                recursive(op + 1, cl)
                temp.pop()

            if cl < op:
                temp.append(")")
                recursive(op, cl + 1)
                temp.pop()

        recursive(0, 0)

        return ans
