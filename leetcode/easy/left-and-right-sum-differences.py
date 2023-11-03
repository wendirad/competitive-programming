class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftSum = 0
        rightSum = sum(nums)

        ans = []
        for num in nums:
            rightSum -= num
            ans.append(
                abs(leftSum - rightSum)
            )
            leftSum += num
        
        return ans