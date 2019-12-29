class LinkNode:
    def __init__(self, data, p = 0):
        self.data = data
        self.next = p
        #self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    def initListTail(self, data):
        self.head = LinkNode(data[0])
        n = self.head
        for i in range(1, len(data)):
            node = LinkNode(data[i])
            n.next = node
            n = n.next
        print("init:", end=" ")
        self.readList()

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def readList(self):
        if self.isEmpty():
            print("empty list")
            return

        node = self.head
        print(node.data, end=",")
        while node.next != 0:
            node = node.next
            print(node.data, end=",")
        print("")

    def getLength(self):
        if self.isEmpty():
            return 0
        count = 1
        node = self.head
        while node.next != 0:
            count += 1
            node = node.next
        return count

    # 在索引值为 index 的节点后插入节点key
    def insertElem(self, key, index):
        if self.isEmpty():
            print("Error Empty List")
            return False

        j = 1
        node = self.head
        while node.next != 0 and j < index:
            node = node.next
            j += 1

        if j < index:
            print("Error")
            return False

        new_node = LinkNode(key)
        tmp = node.next
        node.next = new_node
        new_node.next = tmp

        print("After insert:", end=" ")
        self.readList()

        return True

    # 删除第 index 个节点后的那一个节点
    def deleteElem(self, index):
        if self.isEmpty():
            print("Error Empty List")
            return False

        j = 1
        node = self.head
        while node.next != 0 and j < index-1:
            node = node.next
            j += 1

        #print(j, index)
        if j > index:
            print("Error")
            return False

        node.next = node.next.next

        print("After delete:", end=" ")
        self.readList()

    # 反转链表并输出反转后链表的头结点
    def reverseLinkedList(self):
        if self.isEmpty():
            print("Error")
            return False

        node = self.head
        r_node = LinkNode(node.data)
        while node.next != 0:
            node = node.next
            new_node = LinkNode(node.data)
            new_node.next = r_node
            r_node = new_node

        r = LinkList()
        r.head = r_node

        print("After reverse:", end=" ")
        r.readList()

    # 2.1
    def deleteDups(self):
        if self.isEmpty():
            print("Error")
            return False

        f_node = self.head
        while f_node != 0:
            s_node = f_node
            while s_node.next != 0:
                if f_node.data == s_node.next.data:
                    s_node.next = s_node.next.next
                else:
                    s_node = s_node.next
            f_node = f_node.next

        print("After deleteDups:", end=" ")
        self.readList()

    # 2.2 递归法
    def nthToLast(self, node: LinkNode, k):
        if node == 0:
            return 0

        total = self.nthToLast(node.next, k) + 1
        if total == k:
            print("(1) k'th node: ", node.data)

        return total

    # 2.2 迭代法
    # p1,p2两个指针
    # p2先移动k个节点
    # 然后以相同速度同时移动p1,p2至p2结束
    # 此时p1刚好指向倒数第k个节点
    def nthToLast2(self, k):
        if self.isEmpty():
            print("Error")
            return False

        p1 = self.head
        p2 = self.head

        #for i in range(k-1):
        for i in range(k):
            p2 = p2.next
        #print("p2:", p2.data)

        #while p2.next != 0:
        while p2 != 0:
            #print("p1:", p1.data)
            p1 = p1.next
            p2 = p2.next
        print("(2) k'th node: ", p1.data)

    # 2.4
    def partition(self, x):
        if self.isEmpty():
            print("Error")
            return False

        l_before = LinkList()
        l_after = LinkList()
        n_before = l_before.head
        n_after = l_after.head

        node = self.head
        while node != 0:
            n = LinkNode(node.data)
            if node.data < x:
                if l_before.isEmpty():
                    l_before.head = n
                    n_before = l_before.head
                else:
                    n_before.next = n
                    n_before = n_before.next
            else:
                if l_after.isEmpty():
                    l_after.head = n
                    n_after = l_after.head
                else:
                    n_after.next = n
                    n_after = n_after.next

            node = node.next

        #l_before.readList()
        #l_after.readList()
        node = self.head
        if not l_before.isEmpty():
            n_before = l_before.head
            while n_before != 0:
                node.data = n_before.data
                node = node.next
                n_before = n_before.next
        if not l_after.isEmpty():
            n_after = l_after.head
            while n_after != 0:
                node.data = n_after.data
                node = node.next
                n_after = n_after.next
        print("after partition:", end=" ")
        self.readList()

l = LinkList()
print("read []:", end=" ")
l.readList()
l.initListTail([1,2,3,4])
print("len:", l.getLength())
l.insertElem(3,4)
l.deleteElem(1)
l.reverseLinkedList()

#2.1
d = LinkList()
d.initListTail([1,2,3,4,4,3,2,2])
d.deleteDups()

# 2.2
l = LinkList()
l.initListTail([1,2,3,4,5,6,7,8])
l.nthToLast(l.head, 2)
l.nthToLast2(2)

# 2.4
l = LinkList()
l.initListTail([1,2,3,4,4,3,2,2])
l.partition(3)

# 2.5
def addLists(l1: LinkList, l2: LinkList):
    carry = 0
    l = LinkList()
    n1 = l1.head
    n2 = l2.head
    while n1 != 0 and n2 != 0:
        num = n1.data + n2.data + carry
        if num >= 10:
            num = num%10
            carry = 1
        else:
            carry = 0

        if l.isEmpty():
            l.head = LinkNode(num)
            node = l.head
        else:
            n = LinkNode(num)
            node.next = n
            node = node.next

        n1 = n1.next
        n2 = n2.next

    while n1 != 0:
        if carry > 0:
            n = LinkNode(n1.data+1)
            carry = 0
        else:
            n = LinkNode(n1.data)
        node.next = n
        node = node.next
        n1 = n1.next
        
    while n2 != 0:
        if carry > 0:
            n = LinkNode(n2.data+1)
            carry = 0
        else:
            n = LinkNode(n2.data)
        node.next = n
        node = node.next
        n2 = n2.next

    print("after addLists:", end=" ")
    l.readList()

l1 = LinkList()
l1.initListTail([1,2,4,9])
l2 = LinkList()
l2.initListTail([1,2,8,1,1])
addLists(l1, l2)
