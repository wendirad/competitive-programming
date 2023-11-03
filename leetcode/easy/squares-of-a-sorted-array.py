class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = list(map(lambda x: x**2, nums))
        nums.sort()
        return nums
        