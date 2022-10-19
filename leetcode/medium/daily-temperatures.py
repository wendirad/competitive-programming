class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        
        stk = []
        for ix, i in enumerate(temperatures):
            while stk and i > temperatures[stk[-1]]:
                idx = stk.pop()
                ans[idx] = ix - idx
            stk.append(ix)
        return ans