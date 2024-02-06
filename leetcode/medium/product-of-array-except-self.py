from functools import reduce


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n
        post = [1] * n

        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i - 1]
            post[n - i - 1] = post[n - i] * nums[n - i]

        return [pre[i] * post[i] for i in range(n)]
