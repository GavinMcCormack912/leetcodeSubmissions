# Last updated: 8/12/2025, 9:05:26 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inHash = {}
        for idx, val in enumerate(inorder):
            inHash[val] = idx
        
        
        head = TreeNode(preorder[0])
        rootStack = []
        rootStack.append(head)

        for val in preorder[1:]:
            newNode = TreeNode(val)
            if rootStack and inHash[val] < inHash[rootStack[-1].val]:
                rootStack[-1].left = newNode
            else:
                # pop stack to get to last node greater 
                recent = None
                while rootStack and inHash[val] > inHash[rootStack[-1].val]:
                    recent = rootStack.pop()

                recent.right = newNode
            rootStack.append(newNode)
        return head
