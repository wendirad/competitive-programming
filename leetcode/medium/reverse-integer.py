class Solution:
    def reverse(self, x: int) -> int:
        n = 0
        i = 0
        if x < 0:
            neg = True
        else:
            neg = False

        x = abs(x)

        while x != 0:
            r = x % 10
            x = int(x / 10)
            n = n * 10 + r
            i += 1

        if abs(n) > (2**31 - 1):
            return 0

        return -n if neg else n
