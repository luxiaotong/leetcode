class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

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

# 4.1
def get_depth(node):
    if node == None:
        return 0
    return max(get_depth(node.left), get_depth(node.right)) + 1

def is_balanced(node):
    if node == None:
        return True
    left_depth = get_depth(node.left)
    right_depth = get_depth(node.right)

    if abs(left_depth - right_depth) <= 1:
        return is_balanced(node.left) and is_balanced(node.right)
    else:
        return False

tree = Node('A',Node('B',Node('D'),Node('E')),Node('C',Node('F'),Node('G')))
print("depth: ", get_depth(tree))

tree = Node(
    'A',
    Node(
        'B',
        Node('D'),
        Node('E', Node('H', Node('I', None, None), None))
    ),
    Node(
        'C',
        Node('F'),
        Node('G')
    )
)
print("is balanced: ", is_balanced(tree))
