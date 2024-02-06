class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        n = len(nums)

        while i < n:
            if nums[i] == nums[i - 1]:
                nums.pop(i)
                n -= 1
            else:
                i += 1

        return len(nums)
