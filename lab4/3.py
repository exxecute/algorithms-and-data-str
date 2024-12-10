from typing import List
# Topological sort
# O(m * n), where m = rows, n = columns

NEIGBORS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        m, n = len(matrix), len(matrix[0])

        in_degree = [[0] * n for _ in range(m)]
        longest = [[1] * n for _ in range(m)]

        stack = []

        # Populate in-degree matrix and stack
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j]:
                    in_degree[i][j] += 1
                if i + 1 < m and matrix[i + 1][j] > matrix[i][j]:
                    in_degree[i][j] += 1
                if j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j]:
                    in_degree[i][j] += 1
                if j + 1 < n and matrix[i][j + 1] > matrix[i][j]:
                    in_degree[i][j] += 1
                if in_degree[i][j] == 0:
                    stack.append((i, j))

        while stack:
            x, y = stack.pop()
            for dx, dy in NEIGBORS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] < matrix[x][y]:
                    longest[nx][ny] = max(longest[nx][ny], longest[x][y] + 1)
                    in_degree[nx][ny] -= 1
                    if in_degree[nx][ny] == 0:
                        stack.append((nx, ny))

        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result, longest[i][j])

        return result