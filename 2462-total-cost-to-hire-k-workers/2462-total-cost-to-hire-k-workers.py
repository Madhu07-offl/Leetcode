class Solution:
    def totalCost(self, costs, k, candidates):
        n = len(costs)

        if 2 * candidates >= n:
            return sum(heapq.nsmallest(k, costs))

        left_heap = costs[:candidates]
        right_heap = costs[n - candidates:]

        heapq.heapify(left_heap)
        heapq.heapify(right_heap)

        left = candidates
        right = n - candidates - 1
        total = 0

        for _ in range(k):
            if not right_heap or (left_heap and left_heap[0] <= right_heap[0]):
                total += heapq.heappop(left_heap)

                if left <= right:
                    heapq.heappush(left_heap, costs[left])
                    left += 1
            else:
                total += heapq.heappop(right_heap)

                if left <= right:
                    heapq.heappush(right_heap, costs[right])
                    right -= 1

        return total