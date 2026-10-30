
import heapq
from collections import defaultdict

class Solution:
    def shortestPath(self, n, edges, labels, k):
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))

        pq = [(0, 0, 1)]
        dist = {(0, 1): 0}

        while pq:
            d, u, cnt = heapq.heappop(pq)

            if d != dist[(u, cnt)]:
                continue

            if u == n - 1:
                return d

            for v, w in g[u]:
                nc = cnt + 1 if labels[u] == labels[v] else 1

                if nc > k:
                    continue

                nd = d + w
                if nd < dist.get((v, nc), float('inf')):
                    dist[(v, nc)] = nd
                    heapq.heappush(pq, (nd, v, nc))

        return -1
