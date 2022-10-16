import statistics as sts

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = [0] * len(nums)
        mead = sts.median(nums)
        odinx = 1
        evinx = 0
        for i in nums:
            if i < mead:
                n[odinx] = i
                odinx += 2
            else:
                n[evinx] = i
                evinx += 2
        return n
        