from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        perimeter = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    perimeter += 4
                    if x > 0 and grid[x-1][y] == 1:
                        perimeter -= 2
                    if y > 0 and grid[x][y-1] == 1:
                        perimeter -= 2

        return perimeter
    
print(Solution().islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))