class Solution(object):
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2

            hours = sum((pile + mid - 1) // mid for pile in piles)

            if hours <= h:
                right = mid
            else:
                left = mid + 1

        return left