# Last updated: 8/12/2025, 9:05:22 PM
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # head is the least recently used, tail is most recent (like a queue)
        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        node.next = self.tail
        node.prev = self.tail.prev

        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            #change its position to most recently used
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            #return value
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            #change its position to most recently used
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            #change
            node.val = value
        else:
            new_node = Node(key,value)
            self.cache[key] = new_node
            self.insert(new_node)
            
            if len(self.cache) > self.capacity:
                del self.cache[self.head.next.key]
                self.remove(self.head.next)
            
        
