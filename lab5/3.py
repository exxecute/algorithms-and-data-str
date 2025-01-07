from typing import List
from collections import defaultdict
# kahn's algorythm

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list) 
        incoming = defaultdict(int) 

        for dst, src in prerequisites:
            adjList[src].append(dst)
            incoming[dst] += 1
            
        noIncomingQueue = []
        for src in range(numCourses):
            if incoming[src] == 0:
                noIncomingQueue.append(src)

        count = 0
        while noIncomingQueue:
            src = noIncomingQueue.pop(0)
            count += 1
            for dst in adjList[src]:
                incoming[dst] -= 1
                if incoming[dst] == 0:
                    noIncomingQueue.append(dst)

        return count == numCourses
    

sol = Solution()
print(sol.canFinish(2, [[1,0]]))
print(sol.canFinish(20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]))

5 - 5