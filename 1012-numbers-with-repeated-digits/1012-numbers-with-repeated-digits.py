class Solution:
    def numDupDigitsAtMostN(self, n):
        s = str(n)
        m = len(s)

        def perm(a, b):
            res = 1
            for i in range(b):
                res *= a - i
            return res

        unique = 0

        for length in range(1, m):
            unique += 9 * perm(9, length - 1)

        used = set()

        for i, ch in enumerate(s):
            digit = int(ch)

            for d in range(0 if i else 1, digit):
                if d not in used:
                    unique += perm(9 - i, m - i - 1)

            if digit in used:
                break

            used.add(digit)
        else:
            unique += 1

        return n - unique