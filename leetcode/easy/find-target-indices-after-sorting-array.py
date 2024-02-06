class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        inx = []
        nums.sort()
        for idx, i in enumerate(nums):
            if i == target:
                inx.append(idx)
        return inx
