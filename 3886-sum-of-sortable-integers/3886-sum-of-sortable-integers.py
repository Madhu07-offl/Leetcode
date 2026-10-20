
class Solution(object):
    def sortableIntegers(self, nums):
       
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True
            prev_max = -1

            for i in range(0, n, k):
                block = nums[i:i + k]

                if min(block) < prev_max:
                    valid = False
                    break

                descents = 0
                for j in range(k):
                    if block[j] > block[(j + 1) % k]:
                        descents += 1

                if descents > 1:
                    valid = False
                    break

                prev_max = max(block)

            if valid:
                ans += k

        return ans
