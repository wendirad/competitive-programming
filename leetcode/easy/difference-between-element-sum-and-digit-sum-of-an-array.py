class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        eSum = sum(nums)
        dSum = sum(map(int, ''.join(map(str, nums))))

        return abs(eSum - dSum)