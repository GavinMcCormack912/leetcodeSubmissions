# Last updated: 8/12/2025, 9:05:26 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        numsum = 0
        if not root:
            return False
        
        def dfsPath(root):
            nonlocal numsum
            if not root:
                return False
            # add value. check if you got to the targetSum. MAKE SURE ITS A LEAF
            numsum += root.val
            if numsum == targetSum and not root.left and not root.right:
                return True
            #go down different paths. if a path reaches targetSum if will backtrack to True
            if dfsPath(root.left):
                return True
            if dfsPath(root.right):
                return True

            # no path from current node found, subtract from numsum before returning to previous position
            numsum -= root.val
            return False

        return dfsPath(root)