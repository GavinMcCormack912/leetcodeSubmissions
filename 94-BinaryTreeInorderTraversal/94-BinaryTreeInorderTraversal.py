# Last updated: 8/12/2025, 9:05:28 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        nodeList = []

        def inorder(root):
            if not root:
                return

            inorder(root.left)
            nodeList.append(root.val)
            inorder(root.right)

        inorder(root)
        return nodeList
