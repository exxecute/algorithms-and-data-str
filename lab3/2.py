from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        count = 0
        stack = []

        for i in range(n):
            if not visited[i]:
                stack.append(i)
                while stack:
                    node = stack.pop()
                    if not visited[node]:
                        visited[node] = True
                        for j in range(n):
                            if isConnected[node][j] == 1 and not visited[j]:
                                stack.append(j)
                count += 1

        return count