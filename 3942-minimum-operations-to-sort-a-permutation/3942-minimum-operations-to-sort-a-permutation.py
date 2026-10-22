
class Solution:
    def minOperations(self, nums):
        n = len(nums)
        if n == 1:
            return 0

        inc = dec = 0

        for i in range(n):
            if (nums[(i + 1) % n] - nums[i]) % n != 1:
                inc += 1
            if (nums[i] - nums[(i + 1) % n]) % n != 1:
                dec += 1

        ans = float('inf')
        p = nums.index(0)

        if inc == 0:
            ans = min(ans, p, n - p + 2)

        if dec == 0:
            ans = min(ans, n - p, p + 2)

        return -1 if ans == float('inf') else ans
