class Solution:
    def numOfWays(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        C = [[1] * (n + 1) for _ in range(n + 1)]

        for i in range(2, n + 1):
            for j in range(1, i):
                C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD

        def dfs(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]

            ways = C[len(arr)-1][len(left)]
            return ways * dfs(left) * dfs(right) % MOD

        return (dfs(nums) - 1) % MOD