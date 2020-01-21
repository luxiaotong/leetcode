class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def initListTail(data):
    if data == []:
        return None
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

def rotateRight(head: ListNode, k: int) -> ListNode:
    if head == None or head.next == None:
        return head

    node = head
    n = 1
    while node.next:
        n += 1
        node = node.next
    node.next = head

    node2 = head
    #k = k % n
    #for i in range(k):
    for i in range(n - k%n - 1):
        node2 = node2.next
    new_head = node2.next
    node2.next = None
    return new_head
    
head = initListTail([1,2,3,4,5])
readList(head)
new_head = rotateRight(head, 2)
readList(new_head)
#
#head = initListTail([0,1,2])
#readList(head)
#new_head = rotateRight(head, 4)
#readList(new_head)
#
#head = initListTail([])
#readList(head)
#new_head = rotateRight(head, 0)
#readList(new_head)

head = initListTail([1,2])
readList(head)
new_head = rotateRight(head, 0)
readList(new_head)
