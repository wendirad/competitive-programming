class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        MAX = float("-inf")
        c = 0
        for i in nums:
            if i == 0:
                MAX = max(MAX, c)
                c = 0
            else:
                c += 1

        MAX = max(MAX, c)

        return MAX
