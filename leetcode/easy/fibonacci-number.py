class Solution:
    def fib(self, n: int) -> int:
        fibs = [0, 1]
        for i in range(2, n + 1):
            fibs.append(fibs[-1] + fibs[-2])
        return fibs[n]
