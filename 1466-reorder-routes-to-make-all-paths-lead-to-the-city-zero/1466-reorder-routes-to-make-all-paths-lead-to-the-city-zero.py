class Solution(object):
    def minReorder(self, n, connections):
        graph = [[] for _ in range(n)]
        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))
        visited = [False] * n
        stack = [0]
        visited[0] = True
        changes = 0
        while stack:
            node = stack.pop()
            for neighbor, cost in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    changes += cost
                    stack.append(neighbor)
        return changes
