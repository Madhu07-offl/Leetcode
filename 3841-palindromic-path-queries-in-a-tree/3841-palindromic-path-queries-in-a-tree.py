
class Solution:
    def palindromePath(self, n, edges, s, queries):
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        order = [0]
        parent[0] = 0

        for u in order:
            for v in g[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    order.append(v)

        size = [1] * n
        heavy = [-1] * n

        for u in reversed(order):
            best = 0
            for v in g[u]:
                if parent[v] == u:
                    size[u] += size[v]
                    if size[v] > best:
                        best = size[v]
                        heavy[u] = v

        head = [0] * n
        pos = [0] * n
        timer = 0
        stack = [(0, 0)]

        while stack:
            u, h = stack.pop()
            while u != -1:
                head[u] = h
                pos[u] = timer
                timer += 1

                for v in g[u]:
                    if parent[v] == u and v != heavy[u]:
                        stack.append((v, v))

                u = heavy[u]

        bit = [0] * (n + 1)
        a = [1 << (ord(c) - 97) for c in s]

        def add(i, x):
            i += 1
            while i <= n:
                bit[i] ^= x
                i += i & -i

        def pref(i):
            res = 0
            while i > 0:
                res ^= bit[i]
                i -= i & -i
            return res

        def get(l, r):
            return pref(r + 1) ^ pref(l)

        for u in range(n):
            add(pos[u], a[u])

        ans = []

        for q in queries:
            t, x, y = q.split()
            u = int(x)

            if t == "update":
                new = 1 << (ord(y) - 97)
                add(pos[u], a[u] ^ new)
                a[u] = new
            else:
                v = int(y)
                mask = 0

                while head[u] != head[v]:
                    if depth[head[u]] < depth[head[v]]:
                        u, v = v, u

                    mask ^= get(pos[head[u]], pos[u])
                    u = parent[head[u]]

                if pos[u] > pos[v]:
                    u, v = v, u

                mask ^= get(pos[u], pos[v])
                ans.append(mask & (mask - 1) == 0)

        return ans
