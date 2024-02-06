class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = float("-inf")
        current_sum = 0
        for i in nums:
            current_sum = max(i, current_sum + i)
            best_sum = max(best_sum, current_sum)
        return best_sum
