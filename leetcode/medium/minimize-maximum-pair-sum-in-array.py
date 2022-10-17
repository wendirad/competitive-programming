class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        mx = 0
        nums.sort()
        for i in range(n // 2):
            mx = max(mx, nums[i] + nums[n - i - 1])
        return mx