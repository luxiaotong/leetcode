class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def initListTail(data):
    head = ListNode(data[0])
    n = head
    for i in range(1, len(data)):
        node = ListNode(data[i])
        n.next = node
        n = n.next
    return head

def readList(head):
    if head == None:
        print("empty list")
        return

    node = head
    print(node.val, end=",")
    while node.next != None:
        node = node.next
        print(node.val, end=",")
    print("")

def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
    if head == None:
        return None

    dummy = ListNode(0)
    dummy.next = head
    node = dummy
    i = 0
    while node:
        if i == m-1:
            p1 = node
        if i == n:
            p2 = node
        i += 1
        node = node.next

    p3 = p1.next
    r_node = ListNode(p3.val)
    r_node.next = p2.next
    for i in range(n-m):
        p3 = p3.next
        new_node = ListNode(p3.val)
        new_node.next = r_node
        r_node = new_node
    new_head = r_node
    p1.next = new_head
    
    return dummy.next

head = initListTail([1,2,3,4,5])
head = reverseBetween(head, 2, 4)
readList(head)
