class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        print(id(nums), nums)
        zeros = []
        l = len(nums)
        for i in range(l):
            if nums[i] == 0:
                zeros.append(i)
        for j in range(len(zeros)):
            i = zeros[j] - j
            nums.append(nums.pop(i))