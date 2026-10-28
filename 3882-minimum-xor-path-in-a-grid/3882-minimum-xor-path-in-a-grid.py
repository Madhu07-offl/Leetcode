
class Solution:
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [set() for _ in range(n)]

        for i in range(m):
            for j in range(n):
                v = grid[i][j]
                if i == 0 and j == 0:
                    dp[j] = {v}
                else:
                    s = set()
                    if i:
                        s.update(x ^ v for x in dp[j])
                    if j:
                        s.update(x ^ v for x in dp[j - 1])
                    dp[j] = s

        return min(dp[-1])
