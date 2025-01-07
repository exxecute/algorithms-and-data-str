from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        updated_board = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                neighbors = 0
                for row in range(-1, 2):
                    for col in range(-1, 2):
                        if row == 0 and col == 0:
                            continue
                        if i + row < 0 or i + row >= len(board):
                            continue
                        if j + col < 0 or j + col >= len(board[0]):
                            continue
                        if board[i + row][j + col] == 1 or board[i + row][j + col] == -1:
                            neighbors += 1
                if board[i][j] == 1 and neighbors < 2 or neighbors > 3:
                    updated_board[i][j] = -1
                elif board[i][j] == 0 and neighbors == 3:
                    updated_board[i][j] = 1
                else:
                    updated_board[i][j] = board[i][j]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if updated_board[i][j] == -1:
                    board[i][j] = 0
                elif updated_board[i][j] == 1:
                    board[i][j] = 1
        board = updated_board