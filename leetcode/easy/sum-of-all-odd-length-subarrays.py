class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)

        res = 0

        for i in range(n):
            start = n - i
            end = i + 1
            total = start * end

            if total % 2 == 0:
                total /= 2
            else:
                total = total // 2 + 1

            res += arr[i] * total

        return int(res)
