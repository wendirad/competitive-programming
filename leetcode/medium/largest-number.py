class Solution:
    def compare(self, n, m):
        return (str(m) + str(n)) > (str(n) + str(m))

    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)

        for i in range(n):
            for j in range(1, n - i):
                if self.compare(nums[j - 1], nums[j]):
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]

        return str(int("".join(map(str, nums))))
