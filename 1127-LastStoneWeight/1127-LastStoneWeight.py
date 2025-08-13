# Last updated: 8/12/2025, 9:05:09 PM
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-n for n in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            y = heapq.heappop(maxHeap) * -1
            x = heapq.heappop(maxHeap) * -1

            if y != x:
                heapq.heappush(maxHeap, -(y-x))
        
        if len(maxHeap) > 0:
            return -1 * maxHeap[0]
        else:
            return 0
        
