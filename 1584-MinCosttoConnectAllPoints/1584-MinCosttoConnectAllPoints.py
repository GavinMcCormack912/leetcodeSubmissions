# Last updated: 11/18/2025, 10:07:52 PM
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {}
        n = len(points)
        minCost = 0

        for i in range(n):
            adj[i] = []
        
        #make adjacency list
        for i in range(n):
            for j in range(n):
                if i != j:
                    # manhattan distance as the weight
                    weight = abs(points[i][0]-points[j][0]) + abs(points[i][1] - points[j][1])
                    adj[i].append([j, weight])
        
        # start minHeap
        minHeap = []
        for neighbor, weight in adj[0]:
            heapq.heappush(minHeap, [weight, 1, neighbor])
        
        # keep visit list. No cycles!
        visit = set()
        visit.add(0)

        while len(visit) < n:
            weight, n1, n2 = heapq.heappop(minHeap)
            if n2 in visit:
                continue
            
            minCost += weight
            visit.add(n2)
            for neighbor, weight in adj[n2]:
                if neighbor not in visit:
                    heapq.heappush(minHeap, [weight, n2, neighbor])

        return minCost
