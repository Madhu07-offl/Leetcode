class Solution(object):
    def successfulPairs(self, spells, potions, success):
        from bisect import bisect_left

        potions.sort()
        m = len(potions)
        result = []

        for spell in spells:
            target = (success + spell - 1) // spell
            index = bisect_left(potions, target)
            result.append(m - index)

        return result
