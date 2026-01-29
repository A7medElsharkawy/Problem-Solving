import heapq
from collections import defaultdict
from typing import List

class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int]
    ) -> int:

        INF = 10**18

        # Build graph
        graph = defaultdict(list)
        for o, c, w in zip(original, changed, cost):
            graph[o].append((c, w))

        # Precompute shortest paths from each letter
        dist = {chr(ord('a') + i): {} for i in range(26)}

        def dijkstra(start):
            pq = [(0, start)]
            best = {start: 0}

            while pq:
                curr_cost, u = heapq.heappop(pq)
                if curr_cost > best[u]:
                    continue

                for v, w in graph[u]:
                    new_cost = curr_cost + w
                    if v not in best or new_cost < best[v]:
                        best[v] = new_cost
                        heapq.heappush(pq, (new_cost, v))

            return best

        # Run Dijkstra from each letter
        for ch in dist:
            dist[ch] = dijkstra(ch)

        # Calculate total cost
        total = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            if t not in dist[s]:
                return -1
            total += dist[s][t]

        return total

""""
timwe complexity: O(V * (E + V) log V) where V is the number of unique characters (at most 26) and E is the number of edges (transformations).
Space complexity: O(V^2) for storing shortest paths between all pairs of characters.
"""