class Solution:
    def minOperations(self, s):
        n = len(s)
        t = ''.join(sorted(s))

        if s == t:
            return 0

        if n == 2:
            return -1

        if (''.join(sorted(s[:-1])) + s[-1] == t or
            s[0] + ''.join(sorted(s[1:])) == t):
            return 1

        if s[0] == max(s) and s.count(s[0]) == 1 and \
           s[-1] == min(s) and s.count(s[-1]) == 1:
            return 3

        return 2