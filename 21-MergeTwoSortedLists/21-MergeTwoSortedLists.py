# Last updated: 8/1/2025, 10:27:23 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2

        curr3 = None
        head3 = None

        while curr1 or curr2:
            min_node = None
            curr1val = None
            curr2val = None
            # get node values
            if curr1:
                curr1val = curr1.val
                min_node = curr1
            if curr2:
                curr2val = curr2.val
                #set min_node (to be added next). it defaults to curr1. if curr2 exists, compare 
                # with curr1's value. if it is lower, replace min_node w/ curr2. do .next on
                # whichever node wins
                if min_node:
                    if curr2val < curr1val:
                        min_node = curr2
                        curr2=curr2.next
                    else:
                        curr1 = curr1.next
                else: #min_node is empty. therefore, there was no first list node
                    min_node = curr2
                    curr2=curr2.next
            #if no curr2. only curr1 exists
            else:
                #traverse list 1!
                curr1 = curr1.next

                
            if head3:
                curr3.next = min_node
                curr3 = min_node
            else:
                head3 = min_node
                curr3 = min_node

        return head3


            
