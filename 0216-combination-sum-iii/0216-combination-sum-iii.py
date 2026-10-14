class Solution(object):
    def combinationSum3(self, k, n):
        result = []

        def backtrack(start, path, remaining):
            if len(path) == k:
                if remaining == 0:
                    result.append(path[:])
                return

            for i in range(start, 10):
                if i > remaining:
                    break

                path.append(i)
                backtrack(i + 1, path, remaining - i)
                path.pop()

        backtrack(1, [], n)
        return result