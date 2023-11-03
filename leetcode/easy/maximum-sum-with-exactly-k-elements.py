class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        M = max(nums)
        
        return int((k * (2*M + (k - 1))) / 2)

        