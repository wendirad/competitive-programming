class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        x = num - 3
        if x % 3 != 0:
            return []
        x //= 3
        return [x, x + 1, x + 2]
