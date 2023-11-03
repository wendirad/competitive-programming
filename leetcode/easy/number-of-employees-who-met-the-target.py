class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        c = 0
        for h in hours:
            if h >= target:
                c += 1
        return c