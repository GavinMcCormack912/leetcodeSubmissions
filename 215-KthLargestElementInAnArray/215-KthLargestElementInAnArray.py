# Last updated: 8/12/2025, 9:05:18 PM
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # quicksort!

        maxHeap = [-n for n in nums]
        heapq.heapify(maxHeap)

        res = maxHeap[0]
        for i in range(k):
            res = -1 * heapq.heappop(maxHeap)
        return res