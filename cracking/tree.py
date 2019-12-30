#https://www.cnblogs.com/jiuyang/p/7928248.html
class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def pre_order(tree):
    if tree == None:
        return False
    print(tree.data, end = " ")
    pre_order(tree.left)
    pre_order(tree.right)

def post_order(tree):
    if tree == None:
        return False
    post_order(tree.left)
    post_order(tree.right)
    print(tree.data, end = " ")

def in_order(tree):
    if tree == None:
        return False
    in_order(tree.left)
    print(tree.data, end = " ")
    in_order(tree.right)

def level_order(tree):
    if tree == None:
        return False
    queue = []
    queue.append(tree)
    while True:
        if queue == []:
            break
        node = queue[0]
        print(node.data, end=" ")
        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)
        queue.remove(node)

tree = Node('A',Node('B',Node('D'),Node('E')),Node('C',Node('F'),Node('G')))
print("先序:", end=" ")
pre_order(tree)
print()
print("后序:", end=" ")
post_order(tree)
print()
print("中序:", end=" ")
in_order(tree)
print()
print("层序:", end=" ")
level_order(tree)
print()
