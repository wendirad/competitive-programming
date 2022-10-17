from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = Counter(arr)
        n = len(arr)
        cur = n
        ans = 0
        srt = sorted(freq.items(), key=lambda x: x[1])
        while cur > n / 2:
            cur -= srt.pop()[1]
            ans += 1
        
        return ans
            