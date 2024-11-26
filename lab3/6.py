from typing import List
from collections import deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        queue = deque([source])
        visited.add(source)

        while queue:
            vertex = queue.popleft()
            if vertex == destination:
                return True
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        return False