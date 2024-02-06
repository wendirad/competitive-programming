# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        self.left = 1
        self.right = n
        self.bad_version = float("inf")
        return self.binary_search()

    def binary_search(self):
        if self.right < self.left:
            return self.bad_version

        mid = (self.left + self.right) // 2

        if isBadVersion(mid):
            self.right = mid - 1
            self.bad_version = min(self.bad_version, mid)
        else:
            self.left = mid + 1
        return self.binary_search()
