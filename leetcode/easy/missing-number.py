class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        data = dict.fromkeys(nums)

        n = len(data) + 1

        for i in range(n):
            if i not in data:
                return i