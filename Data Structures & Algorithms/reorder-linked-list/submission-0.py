# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Tortoise & Hare to find midpoint
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow now points to mid (e.g [3,4,5,6])

        # Split the halves
        second = slow.next
        slow.next = None # break the list into two halves

        # Reverse second half
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        # second is now slow reverse (e.g [6,5,4,3])

        # Merge them 
        first, second = head, prev
        ldummy = ListNode(0)

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
            
        
        return second
