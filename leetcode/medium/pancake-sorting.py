class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ks = []
        n = len(arr)
        org = arr.copy()
        arr.sort(reverse=True)
        l = None
        for i, j in enumerate(arr):
            idx = org[:l].index(j)
            org[: idx + 1] = reversed(org[: idx + 1])
            ks.append(idx + 1)
            org[: n - i] = list(reversed(org[: n - i]))
            ks.append(n - i)

            l = -(i + 1)

        return ks
