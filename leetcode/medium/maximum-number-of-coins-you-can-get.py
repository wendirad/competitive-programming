class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles) // 3
        piles.sort(reverse=True)
        piles = piles[:-n]
        return sum(piles[::-2])
