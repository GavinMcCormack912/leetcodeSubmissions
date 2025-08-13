# Last updated: 8/12/2025, 9:05:14 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def minNodeValue(node):
            curr = node
            while curr and curr.left:
                curr = curr.left
            return curr
        
        # Tree traversal
        if not root:
            return None
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        # Node found. remove it
        else:
        # Check for 0-1 children
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
        # otherwise, 2 children
            else:
                minNode = minNodeValue(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)
        return root
