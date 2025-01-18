from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        moveList = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if obstacleGrid[i][j] == 1:
                    moveList[i][j] = 0
                elif i == 0 and j == 0:
                    moveList[i][j] = 1
                elif i == 0:
                    moveList[i][j] = moveList[i][j-1]
                elif j == 0:
                    moveList[i][j] = moveList[i-1][j]
                else:
                    moveList[i][j] = moveList[i][j-1] + moveList[i-1][j]

        return moveList[rows-1][cols-1]
                
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Solution().uniquePathsWithObstacles(obstacleGrid)