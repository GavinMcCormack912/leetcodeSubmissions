# Last updated: 8/12/2025, 9:05:08 PM
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distHeap = []

        for row in points:
            dist = math.sqrt(row[0]**2 + row[1]**2)
            distHeap.append((dist, [row[0], row[1]]))
        
        heapq.heapify(distHeap)

        res = []
        for i in range(k):
            tup = heapq.heappop(distHeap)
            res.append(tup[1])
        return res