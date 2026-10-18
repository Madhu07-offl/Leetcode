class Solution:
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        tree = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def update(node, start, end, l, r):
            if l > end or r < start:
                return 0

            if l <= start and end <= r:
                old = tree[node]
                length = end - start + 1
                tree[node] = (old + length) % MOD
                lazy[node] += 1
                return old

            mid = (start + end) // 2
            left = node * 2
            right = left + 1

            if lazy[node]:
                val = lazy[node]
                tree[left] = (tree[left] + val * (mid - start + 1)) % MOD
                tree[right] = (tree[right] + val * (end - mid)) % MOD
                lazy[left] += val
                lazy[right] += val
                lazy[node] = 0

            result = update(left, start, mid, l, r)
            result += update(right, mid + 1, end, l, r)

            tree[node] = (tree[left] + tree[right]) % MOD
            return result % MOD

        last = {}
        ans = 0
        total = 0

        for i, x in enumerate(nums):
            prev = last.get(x, -1)
            l = prev + 1
            r = i

            old_sum = update(1, 0, n - 1, l, r)
            count = r - l + 1

            total = (total + 2 * old_sum + count) % MOD
            ans = (ans + total) % MOD

            last[x] = i

        return ans