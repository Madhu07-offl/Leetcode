class Solution:
    def numTilings(self, n):
        MOD = 10**9 + 7

        if n <= 2:
            return n

        a, b, c = 1, 2, 5

        for i in range(4, n + 1):
            a, b, c = b, c, (2 * c + a) % MOD

        return c