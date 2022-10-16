class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        pairs  = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    pairs += 1
        return pairs
            