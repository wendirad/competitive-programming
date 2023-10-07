class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        idxs = {j:i for i,j in enumerate(nums)}

        for num, val in operations:
            idxs[val] = idxs[num]
            nums[idxs[num]] = val

        return nums