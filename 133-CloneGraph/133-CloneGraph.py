# Last updated: 8/25/2025, 3:36:11 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
    
        res = Node(node.val)
        queue = deque()
        queue.append(node)
        
        # use dict instead of a visited set
        oldVisited = {}
        oldVisited[node] = res
        
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()

                for neighbor in curr.neighbors:
                    if neighbor not in oldVisited:
                        queue.append(neighbor)
                        oldVisited[neighbor] = Node(neighbor.val)
                    oldVisited[curr].neighbors.append(oldVisited[neighbor])
                    
        
        return res