from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        freq = Counter(nums)

        ops = 0
        
        for i in nums:
            if freq[i] < 1:
                continue
            freq[i] -= 1
            target = k - i
            if freq[target] > 0:
                freq[target] -= 1
                ops += 1
        
        return ops
        
