class Solution:
    def maxAlternatingSum(self, nums):
        squares = sorted([x * x for x in nums], reverse=True)
        positive = (len(nums) + 1) // 2
        return sum(squares[:positive]) - sum(squares[positive:])