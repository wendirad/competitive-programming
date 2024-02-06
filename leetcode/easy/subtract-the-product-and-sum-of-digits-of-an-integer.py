class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        S = 0
        P = 1

        while n != 0:
            last = n % 10
            n //= 10
            S += last
            P *= last
        return P - S
