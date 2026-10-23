
class Solution:
    def sortPermutation(self, nums):
        ans = -1
        for i, num in enumerate(nums):
            if i != num:
                if ans == -1:
                    ans = num
                else:
                    ans &= num
        return 0 if ans == -1 else ans
