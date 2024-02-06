class Solution:
    def isValid(self, s: str) -> bool:
        op = ["(", "{", "["]
        cl = [")", "}", "]"]

        stack = []

        for i in s:
            if i in op:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False

                t = stack.pop()

                if op.index(t) != cl.index(i):
                    return False

        if len(stack) != 0:
            return False
        return True
