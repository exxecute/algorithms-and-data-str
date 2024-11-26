from typing import List

class Solution(object):
    def countPairs(self, n: int, edges: List[List[int]]):
        neighbors = [[] for _ in range(n)]
        for edge in edges:
            neighbors[edge[0]].append(edge[1])
            neighbors[edge[1]].append(edge[0])

        visited = [False] * n
        sum_, squaresum = 0, 0

        for i in range(n):
            if not visited[i]:
                stack = [i]
                visited[i] = True
                ans = 0
                while stack:
                    node = stack.pop()
                    ans += 1
                    for neighbor in neighbors[node]:
                        if not visited[neighbor]:
                            stack.append(neighbor)
                            visited[neighbor] = True
                sum_ += ans
                squaresum += ans * ans

        return (sum_ * sum_ - squaresum) // 2