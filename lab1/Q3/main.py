from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.__checkTile(grid, i, j)
                    count += 1

        return count
    
    def __checkTile(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.__checkTile(grid, i+1, j)
        self.__checkTile(grid, i-1, j)
        self.__checkTile(grid, i, j+1)
        self.__checkTile(grid, i, j-1)
        
# grid1 = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# print(Solution().numIslands(grid1))