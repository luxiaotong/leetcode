class LinkNode:
    def __init__(self, k = 0, x = 0):
        self.val = x
        self.key = k
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.hashmap = {}
        self.capacity = capacity
        self.len = 0

        self.head = LinkNode(0, 0)
        self.tail = LinkNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hashmap:
            node = self.hashmap[key]

            node.prev.next = node.next
            node.next.prev = node.prev

            temp = self.head.next
            self.head.next = node
            node.next = temp
            temp.prev = node
            node.prev = self.head

            self.readline()

            return node.val
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        if key not in self.hashmap:
            node = LinkNode(key, value)
            temp = self.head.next
            self.head.next = node
            node.next = temp
            temp.prev = node
            node.prev = self.head
            self.hashmap[key] = node
            self.len += 1

            if self.len > self.capacity:
                temp = self.tail.prev
                del self.hashmap[temp.key]
                self.tail.prev = self.tail.prev.prev
                self.tail.prev.next = self.tail
        else:
            node = self.hashmap[key]
            node.val = value

            node.prev.next = node.next
            node.next.prev = node.prev

            temp = self.head.next
            self.head.next = node
            node.next = temp
            temp.prev = node
            node.prev = self.head
            

        self.readline()


    def readline(self):
        node = self.head
        while node:
            print("next:", node.val, end=", ")
            node = node.next
        print()

        node = self.tail
        while node:
            print("prev:", node.val, end=", ")
            node = node.prev
        print()
        print()



# Your LRUCache object will be instantiated and called as such:
#capacity = 5
#obj = LRUCache(capacity)
#obj.put(1,1)
#obj.put(2,2)
#obj.put(3,3)
#obj.put(4,4)
#obj.put(5,5)
#obj.put(6,6)
#print(obj.get(2))
#obj.put(7,7)

obj = LRUCache(2)
obj.put(2,1)
obj.put(2,2)
obj.get(2)
obj.put(1,1)
obj.put(4,1)
print(obj.get(2))
print(obj.hashmap[4].val)
