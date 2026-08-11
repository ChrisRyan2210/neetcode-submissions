class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if self.size < 0 or index >= self.size:
            return -1
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        node1 = ListNode(val)
        node1.next = self.head
        self.head = node1
        if self.size == 0:
            self.tail = node1
        self.size +=1

    def addAtTail(self, val: int) -> None:
        end_node = ListNode(val)
        if self.size == 0:
            self.head = end_node
            self.tail = end_node
        else:
            self.tail.next = end_node
            self.tail = end_node
        self.size +=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
                return
        
        node = ListNode(val)
        
        # Empty list
        if self.size == 0:
            self.head = node
            self.tail = node
        
        # Add at head
        elif index == 0:
            node.next = self.head
            self.head = node
        
        # Add at tail
        elif index == self.size:
            self.tail.next = node
            self.tail = node
        
        # Add in middle
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            node.next = curr.next
            curr.next = node
        
        self.size += 1
                

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
            if self.size == 1:
                self.tail = None
        else:
            curr = self.head
            for _ in range(index-1):
                curr = curr.next
            curr.next = curr.next.next
            if index == self.size -1:
                self.tail = curr
        self.size -=1
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)