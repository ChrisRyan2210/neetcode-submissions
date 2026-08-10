# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
# trick to make it so we can remove the first node is to add a dummy node before it that points to first node -> then loop from there
# we will also need a point "prev" that points to the previous node -> we will link this node if the current node != val

        dummy = ListNode(next = head)
        prev = dummy

        while head:
            if head.val == val:
                # dont do anything with prev
                head = head.next
                prev.next = head
            else:
                prev.next = head
                prev = head
                head = head.next
        return dummy.next
