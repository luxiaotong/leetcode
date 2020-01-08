#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#

# @lc code=start
class LinkNode:
    def __init__(self, k = 0, x = 0):
        self.val = x
        self.key = k
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.capacity = capacity
        self.len = 0

        self.head = LinkNode(0, 0)
        self.tail = LinkNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]

            node.prev.next = node.next
            node.next.prev = node.prev

            temp = self.head.next
            self.head.next = node
            node.next = temp
            temp.prev = node
            node.prev = self.head

            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
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
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

