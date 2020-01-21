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

def swapPairs(head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        p1 = p2 = dummy
        #[0,1,2,3,4]
        while p2.next and p2.next.next:
            #readList(dummy)
            p2 = p2.next.next

            # 交换
            tmp = p1.next
            #print("p1:", p1.val)
            #print("p2:", p2.val)
            #print("tmp:", tmp.val)
            p1.next = p2
            tmp.next = p2.next
            p2.next = tmp

            #print("p1111:", p1.val)
            p1 = p1.next.next
            #print("p1***:", p1.val)
            p2 = p1
            
        return dummy.next

head = initListTail([1,2,3,4])
head = swapPairs(head)
readList(head)
head = initListTail([1,2,3])
head = swapPairs(head)
readList(head)
