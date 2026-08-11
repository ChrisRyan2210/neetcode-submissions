## we can imagine Browser History as a Doubly Linked List
# Step 1: Write ListNode class and constructor
# Step 2: BrowserHistory __init__ initialises a ListNode with the node.val = str. This will be the first node in the List every time, like opening a new browser. NB** we wont have a "head" really for this - just mark the first node as "curr", this will act as the head, everything stems from this
# Step 3: for visit: it doesnt really matter which steb of the breadcrumb we are on -> we just assign curr.next = to the new Node, and then everything after curr gets garbage collected as there is nothing pointing to it
        # Cases: There can be one node (homepage)
        # or there can be more than one node
        # in either case we know that self.curr will point to a node


## Step 1
class ListNode:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev


class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = ListNode(homepage) # Step 2
        self.base = self.curr # store this so we can use it to make sure steps < x by making sure we break loop if curr node is homepage

    def visit(self, url: str) -> None:
        node = ListNode(url)
        self.curr.next = node # set current nodes ptr to new url/node
        node.prev = self.curr # set new nodes prev ptr to curr
        self.curr = self.curr.next # shift curr to new node (the new url)

    def back(self, steps: int) -> str:
        # validate steps
        if steps < 1:
            return
        # if we are at homepage
        if self.curr == self.base:
            return self.curr.val
        # otherwise we can perform the operation as long as we are not at base
        for _ in range(steps):
            if self.curr == self.base:
                return self.curr.val
            self.curr = self.curr.prev # go back one node
        return self.curr.val
            

    def forward(self, steps: int) -> str:
        # we know the last nodes ptr points to None so we can while loop to it
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps -=1
        return self.curr.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)