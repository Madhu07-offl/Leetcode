
class Solution:
    def findSecretWord(self, words, master):
        def match(a, b):
            return sum(x == y for x, y in zip(a, b))

        candidates = words[:]

        for _ in range(30):
            if not candidates:
                return

            best = None
            score = float('inf')

            for w in words:
                groups = [0] * 7

                for c in candidates:
                    groups[match(w, c)] += 1

                worst = max(groups[:6])

                if worst < score:
                    score = worst
                    best = w

            result = master.guess(best)

            if result == 6:
                return

            candidates = [
                w for w in candidates
                if match(w, best) == result
            ]
