class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        MAX = float('-inf')
        MIN = float('inf')
        SUM = 0
        COUNT = 0
        for i in salary:
            SUM += i
            COUNT += 1
            MAX = max(MAX, i)
            MIN = min(MIN, i)
        SUM -= (MAX + MIN)
        return float('%.5f'%((SUM) / (COUNT - 2)))