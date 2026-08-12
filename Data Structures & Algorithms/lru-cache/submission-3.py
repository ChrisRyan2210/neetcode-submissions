
class ListNode:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def insert(self, node):
        # this handles insertion of node to end of LL (MRU)
        # this will use the right dummy to insert a node at MRU
        node.next = self.right # point node to dummy right
        node.prev = self.right.prev # point node.prev to old MRU
        self.right.prev.next = node # make the old MRU ptr to node
        self.right.prev = node # make right dummy ptr to node

    def remove(self, node):
        # this handles removing a node from its curr position in LL
        node.prev.next = node.next # make prev node point to next node
        node.next.prev = node.prev # make next node prev pt to prev node

    def __init__(self, capacity: int):
        self.cache = {}
        self.size = capacity
        # 2 dummy nodes we can use as a base for our funcs (never change)
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        # point them to each other
        self.left.next = self.right 
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key] # retrieve the node using the key
            value = node.val # get the value from the node
            self.remove(node)
            self.insert(node)
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        # CASE 1: key exists in map (need to check this first)
        if key in self.cache:
            node = self.cache[key] # retrieve the node from cache
            node.val = value # update the nodes value
            self.remove(node) # remove the node from current position in LL 
            self.insert(node) # insert node at MRU
        # CASE 2: if we are below capacity
        elif len(self.cache) < self.size:
            node = ListNode(key, value) # create node (gets next, prev in next ln)
            self.insert(node) # insert the node at MRU using helper func
            self.cache[key] = node # add (key, node) to cache
        else: # CASE 3: key does not exist in map & at capacity
            node = ListNode(key, value)
            self.insert(node) # add node to MRU (we are now above capacity)
            lru_node = self.left.next # retrieve LRU node using dummy left
            self.remove(lru_node)
            self.cache[key] = node # add node to cache map
            del self.cache[lru_node.key] # delete from map O(1)

            
           
