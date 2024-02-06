class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        MAX = max(candies)
        return [i + extraCandies >= MAX for i in candies]
