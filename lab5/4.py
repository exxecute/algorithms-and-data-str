from typing import List
import heapq

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        
        trees = []
        heapq.heapify(trees)
        m = len(forest)
        n = len(forest[0])
        for i in range(m):
            for j in range(n):
                if forest[i][j]>1:
                    heapq.heappush(trees,(forest[i][j],i,j))
        curr = (0,0,0)
        res = 0
        while trees:
            queue = [curr]
            visited = set([(curr[0],curr[1])])
            find = False
            for i,j,d in queue:
                if (i,j) == (trees[0][1],trees[0][2]):
                    forest[i][j] = 1
                    res += d
                    curr = (i,j,0)
                    heapq.heappop(trees)
                    find = True
                    break
                else:
                    for di,dj in [(0,1),(1,0),(0,-1),(-1,0)]:
                        if 0<=i+di<m and 0<=j+dj<n and forest[i+di][j+dj] > 0 and (i+di,j+dj) not in visited:
                            visited.add((i+di,j+dj))
                            queue.append((i+di,j+dj,d+1))
            if not find:
                return -1
        return res