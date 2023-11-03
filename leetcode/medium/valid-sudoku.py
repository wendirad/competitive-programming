class Solution:
    def validateRow(self, board):
        for row in board:
            dup = set()
            n = 0
            for num in row:
                if num == ".":
                    continue
                dup.add(num)
                n += 1
            if n != len(dup):
                return False
        return True
    
    def validateCells(self, board):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                nums = []
                for k in range(3):
                    for l in range(3):
                        if board[i + k][j + l] != ".":
                            nums.append(board[i + k][j + l])
                if len(nums) != len(set(nums)):
                    return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if (
            self.validateRow(board) and
            self.validateRow(zip(*board)) and
            self.validateCells(board)
        ):
            return True
        return False