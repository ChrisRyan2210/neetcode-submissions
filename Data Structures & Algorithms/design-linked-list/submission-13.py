class ListNode():
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.size = 0


    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        curr = self.head.next # set curr = first node (after dummy)
        for _ in range(index): # (4) we want 5th node, so loop 4 times from curr
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head.next # skipping the dummy head node (may be None ptr)
        self.head.next = node
        self.size +=1

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node
        self.size +=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        node = ListNode(val)
        if index == 0:
            self.addAtHead(val)
        else:
            curr = self.head # use dummy here as we want to go to before index
            for _ in range(index):
                curr = curr.next
            node.next = curr.next
            curr.next = node
        self.size +=1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        curr = self.head
        for _ in range(index):
            curr = curr.next
        curr.next = curr.next.next
        self.size -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)