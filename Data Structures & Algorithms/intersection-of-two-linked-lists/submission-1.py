# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
# Think of it like a game of cat and mouse. The goal is for both of the pointers to be pointing to the same point in memory.
# we loop through each list, when we get to the end of the list, we jump to the other list to try and find the other pointer. All the while, that pointer is doing the same thing.
# If there is an intersection, they will eventually meet up at some point during n+m steps. Otherwise, they both end up at null

        l1 = headA
        l2 = headB

        while l1 != l2:
            if l1:
                l1 = l1.next
            else:
                l1 = headB
            if l2:
                l2 = l2.next
            else:
                l2 = headA
        return l1




