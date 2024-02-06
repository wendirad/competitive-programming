class Solution:
    def tribonacci(self, n: int) -> int:
        tri_fib = [0, 1, 1]
        for i in range(3, n + 1):
            tri_fib.append(tri_fib[-1] + tri_fib[-2] + tri_fib[-3])
        return tri_fib[n]
