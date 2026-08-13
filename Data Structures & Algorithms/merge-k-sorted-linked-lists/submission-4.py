# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: 

     # Our actual sorting algo (helper function)
     # because they are sorted we can walk up both and do direct comparison
    def merge(self, l1, l2):
        
        dummy = ListNode(0) # always return dummy.next - this wont change
        curr = dummy
        
        while l1 and l2: 
            if l1.val > l2.val:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
            curr = curr.next

        while l1:
            curr.next = l1
            curr = curr.next
            l1 = l1.next

        while l2:
            curr.next = l2
            curr = curr.next
            l2 = l2.next
        
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # merge_sort algo (pairing up arrays)
        if not lists:
            return None
        
        #BASE CASE 
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                merged.append(self.merge(l1, l2))

            lists = merged

        return lists[0]