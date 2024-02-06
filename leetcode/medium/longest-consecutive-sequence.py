class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 1:
            return n

        nums.sort()
        mx = 1
        cur = 1
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] - 1 == nums[i - 1]:
                cur += 1
            else:
                mx = max(mx, cur)
                cur = 1
        mx = max(mx, cur)

        return mx
