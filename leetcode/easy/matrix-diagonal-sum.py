class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)

        SUM = 0
        for i in range(n):
            SUM += (mat[i][0 + i] + mat[i][n - i - 1])
        
        if n % 2 == 1:
            SUM -= mat[n//2][n//2]
        
        return SUM