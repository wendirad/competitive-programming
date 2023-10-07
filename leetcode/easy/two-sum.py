class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        n = len(nums)

        for i in range(n):
            element = nums[i]
            diff = target - element
            if diff in sums:
                return [sums[diff], i]
            
            sums[element] = i