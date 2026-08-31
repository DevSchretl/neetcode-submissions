class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        group = []

        for i in range(9):

            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in group:
                        return False
                    else:
                        group.append(board[i][j])
            
            group = []

            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in group:
                        return False
                    else:
                        group.append(board[j][i])
            
            group = []

            for j in range(9):
                if board[3*(i//3) + j//3][3*(i%3) + (j%3)] != ".":
                    if board[3*(i//3) + j//3][3*(i%3) + (j%3)] in group:
                        return False
                    else:
                        group.append(board[3*(i//3) + j//3][3*(i%3) + (j%3)])
            
            group = []
        
        return True



        