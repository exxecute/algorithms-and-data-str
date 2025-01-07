from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        updated_board = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        neighborPoints = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        max_y = len(board)
        max_x = len(board[0])
        for y in range(len(board)):
            for x in range(len(board[0])):
                neighbors = 0
                for neighborPoint in neighborPoints:
                    if ((neighborPoint[0] + x)) >= 0 and ((neighborPoint[0] + x) < max_x) and ((neighborPoint[1] + y) >= 0) and ((neighborPoint[1] + y) < max_y):
                        neighbors += board[neighborPoint[1] + y][neighborPoint[0] + x]
                cell = 0
                if neighbors == 2 or neighbors == 3:
                    if board[y][x] == 1:
                        cell = 1
                    else:
                        if neighbors == 3:
                            cell = 1
                updated_board[y][x] = cell
        for y in range(len(board)):
            for x in range(len(board[0])):
                board[y][x] = updated_board[y][x]


board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Solution().gameOfLife(board)
print(board)

# 0 1
# 0 0


# 1
# >2    0
# =2,3  1
# <3    0

# 0
# =3    1