
class Solution:
    def closedIsland(self, grid):
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            stack = [(r, c)]
            grid[r][c] = 1
            closed = True

            while stack:
                x, y = stack.pop()

                if x == 0 or y == 0 or x == m - 1 or y == n - 1:
                    closed = False

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        stack.append((nx, ny))

            return closed

        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if dfs(i, j):
                        count += 1

        return count
