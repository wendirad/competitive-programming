class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_sorted = sorted(nums)
        answer = []
        for i in nums:
            answer.append(nums_sorted.index(i))
        return answer