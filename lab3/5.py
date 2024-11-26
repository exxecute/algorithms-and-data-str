from typing import List
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        colorList=[-1]*n
        for i in range(n):
            if colorList[i]!=-1:
                continue

            q=deque()
            q.append((i,0))
            while q:
                node,color=q.popleft()
                if colorList[node]==-1:
                    colorList[node]=color
                    for nx in graph[node]:
                        q.append((nx,color^1))


                if colorList[node]!=color:
                    return False

        return True