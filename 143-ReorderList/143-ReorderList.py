# Last updated: 8/1/2025, 10:27:17 PM
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []

        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        left, right = 0, len(nodes) - 1
        while left < right:
            nodes[left].next = nodes[right]
            left += 1
            if left >= right:
                continue
            nodes[right].next = nodes[left]
            right -= 1
        nodes[left].next = None