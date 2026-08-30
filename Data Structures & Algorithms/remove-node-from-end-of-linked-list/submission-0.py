# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Dummy nodes will help with edge cases and where len = 1
        l = 0 
        curr = head
        while curr:
            l += 1
            curr = curr.next
        ctr = l - n

        dummy = ListNode(0, head)
        curr = dummy 
        while ctr > 0:
            curr = curr.next
            ctr -= 1
        curr.next = curr.next.next
        
        return dummy.next


