# Last updated: 8/1/2025, 10:27:18 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        indexList = []
        curr = head
        
        while curr:
            if curr in indexList:
                #loop_idx = indexList.index(curr)
                return True
            indexList.append(curr)
            curr = curr.next

        return False