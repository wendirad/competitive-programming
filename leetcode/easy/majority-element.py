from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        MAX = 0
        MAX_N = None
        
        for i in nums:
            freq[i] += 1
            if freq[i] > MAX:
                MAX = freq[i]
                MAX_N = i
        return MAX_N
        
        