from typing import List
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0
  
        totalCost = 0
        visited = set()
        
        distances = [float('inf')] * n
        
        start_node = 0
        distances[start_node] = 0
        
        minHeap = [(0, start_node)]  
        
        while minHeap:
            dist, current = heapq.heappop(minHeap)
            
            if current in visited:
                continue
            
            visited.add(current)
            totalCost += dist
            
            for i in range(n):
                if i not in visited:
                    calculatedDist = abs(points[current][0] - points[i][0]) + abs(points[current][1] - points[i][1])
                    
                    if calculatedDist < distances[i]:
                        distances[i] = calculatedDist
                        heapq.heappush(minHeap, (calculatedDist, i))
        
        return totalCost