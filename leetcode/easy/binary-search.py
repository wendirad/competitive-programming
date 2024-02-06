class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        self.nums = nums
        self.target = target
        return self.binary_search(left, right)

    def binary_search(self, left, right):
        if right < left:
            return -1
        mid = (left + right) // 2

        if self.nums[mid] == self.target:
            return mid
        elif self.nums[mid] < self.target:
            left = mid + 1
        else:
            right = mid - 1
        return self.binary_search(left, right)
