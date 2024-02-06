from collections import defaultdict


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup = defaultdict(int)

        for num in nums:
            dup[num] += 1
            if dup[num] > 1:
                return True

        return False
