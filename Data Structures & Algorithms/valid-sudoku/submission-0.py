class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for char in row:
                if char != ".":
                    if char in seen:
                        return False
                    seen.add(char)

        for column in range(9):
            seen = set()
            for row in board:
                char = row[column]
                if char != ".":
                    if char in seen:
                        return False
                    seen.add(char) 
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        val = board[r + i][c + j]
                        if val != ".":
                            if val in seen:
                                return False
                            seen.add(val)

             
        return True