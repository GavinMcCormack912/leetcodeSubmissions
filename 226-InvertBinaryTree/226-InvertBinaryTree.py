# Last updated: 8/1/2025, 10:27:13 PM

class Solution:
    def invertSides(self, root):
        if not root:
            return
        #otherwise, switch children and go to each of them afterwards
        temp = root.right
        root.right = root.left
        root.left = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invertSides(root)
        return root