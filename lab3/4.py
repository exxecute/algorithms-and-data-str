from typing import List

class Solution:
    def longestCycle(self, edges: List[int]):
        cycleLength = [-1] * len(edges) 
        visited = [False] * len(edges) 
        maxLength = -1  
        
        for i in range(len(edges)): 
            if not visited[i]: 
                visited[i] = True 
                destination = edges[i] 
                length = 1  
                nodeToDistance = {} 
                nodeToDistance[i] = 0  
                
                while destination != -1 and not visited[destination]:
                    nodeToDistance[destination] = length  
                    visited[destination] = True  
                    destination = edges[destination] 
                    length += 1 
                
                if destination != -1 and destination in nodeToDistance:
                    cycleLength[destination] = length - nodeToDistance[destination]
                    maxLength = max(maxLength, length - nodeToDistance[destination])
        
        return maxLength