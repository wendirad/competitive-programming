class Solution:
    def is_art(self, nums):
        nums.sort()
        diff = nums[1] - nums[0]
        n = len(nums)
        
        for i in range(1, n-1):
            ciff = nums[i+1] - nums[i]
            if diff != ciff:
                return False
        
        return True
        
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        return [self.is_art(nums[i : j+1]) for i, j in zip(l, r)]
            