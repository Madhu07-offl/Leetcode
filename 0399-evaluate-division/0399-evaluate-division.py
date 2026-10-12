class Solution(object):
    def calcEquation(self, equations, values, queries):
        graph = {}

        for (a, b), value in zip(equations, values):
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []

            graph[a].append((b, value))
            graph[b].append((a, 1.0 / value))

        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0

            if start == end:
                return 1.0

            visited.add(start)

            for neighbor, value in graph[start]:
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    if result != -1.0:
                        return value * result

            return -1.0

        result = []

        for a, b in queries:
            result.append(dfs(a, b, set()))

        return result