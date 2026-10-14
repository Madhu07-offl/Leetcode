class Solution(object):
    def maxSumOfSquares(self, num, sum):
        if sum > 9 * num:
            return ""
        full, rem = divmod(sum, 9)
        result = "9" * full
        if rem > 0:
            result += str(rem)
        result += "0" * (num - len(result))
        return result