class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0

        ans = [nums[0]]

        for i in nums[1:]:
            ans.append(ans[-1] + i)

        return ans
