from typing import List
# O(n)

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for size, target in edges:
            graph[size].append(target)
            graph[target].append(size)
        
        count = [0] * n
        ans = [0] * n

        count[0] = 1
        stack = [(n, 0) for n in graph[0]]
        while stack: # Calculate subtree size and sum of distances for each node
            node, parent = stack[-1]
            if count[node] == 0:
                count[node] = 1
                for neighbour in graph[node]:
                    if neighbour == parent:
                        continue
                    stack.append((neighbour, node))
            else:
                stack.pop()
                ans[parent] += ans[node] + count[node]
                ans[node] = 0
                count[parent] += count[node]

        stack = [0]
        while stack:# Recalculate sum of distances for each node
            node = stack.pop()
            for neighbour in graph[node]:
                if ans[neighbour]:
                    continue
                ans[neighbour] = ans[node] + n - 2 * count[neighbour]
                stack.append(neighbour)

        return ans