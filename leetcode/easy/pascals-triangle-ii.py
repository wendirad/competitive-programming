from math import factorial


class Solution:
    def bin_cof(self, n, k):
        return (factorial(n)) // (factorial(k) * factorial(n - k))

    def getRow(self, rowIndex: int) -> List[int]:
        cofs = []
        for i in range(rowIndex + 1):
            cofs.append(self.bin_cof(rowIndex, i))

        return cofs
