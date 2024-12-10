import heapq
from collections import defaultdict
from typing import List
# O(n * log(n)), log(n)из-за двоичной кучи

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        root = k
        nodes_count = n

        graph = defaultdict(list)
        for source, target, time in times:
            graph[source].append((target, time))

        visited = set()

        # priority queue with appended root
        priority_queue = [(0, root)]

        distances = [float('inf')] * (nodes_count + 1)
        distances[root] = 0

        while priority_queue: # Dijkstra’s algorithm
            # get the minimal distance and node
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_node in visited:
                continue

            for neighbor, time in graph[current_node]:
                new_distance = current_distance + time
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor))

        # delete first element, since it's not used
        del distances[0]

        for d in range(len(distances)):
            if distances[d] == float('inf'):
                return -1

        return max(distances)
