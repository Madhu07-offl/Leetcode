class Solution:
    def minSwaps(self, nums):
        n = len(nums)

        def digitSum(x):
            return sum(int(d) for d in str(x))

        sorted_nums = sorted(nums, key=lambda x: (digitSum(x), x))

        pos = {num: i for i, num in enumerate(sorted_nums)}

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i]:
                continue

            cycle = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = pos[nums[j]]
                cycle += 1

            if cycle > 1:
                swaps += cycle - 1

        return swaps