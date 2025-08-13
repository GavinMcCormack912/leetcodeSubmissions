# Last updated: 8/12/2025, 9:05:16 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        val = None
        k_smallest = 0
        def inorderK(root):
            nonlocal val
            nonlocal k_smallest
            if not root:
                return
            if val:
                return
            
            
            inorderK(root.left)
            k_smallest += 1
            if k_smallest == k:
                val = root.val
            inorderK(root.right)
        
        inorderK(root)
        return val


            