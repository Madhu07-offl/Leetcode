class Solution:
    def minFlips(self, a, b, c):
        flips = 0

        while a or b or c:
            x = a & 1
            y = b & 1
            z = c & 1

            if z == 0:
                flips += x + y
            elif x == 0 and y == 0:
                flips += 1

            a >>= 1
            b >>= 1
            c >>= 1

        return flips