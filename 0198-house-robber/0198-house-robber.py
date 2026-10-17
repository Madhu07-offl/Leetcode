class Solution:
    def rob(self, nums):
        prev1 = 0
        prev2 = 0

        for num in nums:
            current = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = current

        return prev1