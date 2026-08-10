# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

# Tortoise and Hare to find the middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
# slow now points to the start of the second half

# Reverse the second half
        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
# now prev points to head of reversed
# prev = [1, 2, 3]

# compare both halves
        left = head
        right = prev

        while right: # right will end first
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
