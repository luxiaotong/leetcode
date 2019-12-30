#https://blog.csdn.net/u010089444/article/details/70854510
#https://blog.csdn.net/u011608357/article/details/35785553
class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def insert(node, val):
    if node == None:
        node = Node(val, None, None)
    elif val < node.data:
        node.left = insert(node.left, val)
    elif val > node.data:
        node.right = insert(node.right, val)

    return node

def query(node, parent, val):
    if node == None:
        return False, node, parent
    elif val == node.data:
        return True, node, parent
    elif val < node.data:
        return query(node.left, node, val)
    elif val > node.data:
        return query(node.right, node, val)

def findmin(node):
    if node == None:
        return False
    
    if node.left == None:
        return node.data
    else:
        return findmin(node.left)

def findmax(node):
    if node == None:
        return False
    
    if node.right == None:
        return node.data
    else:
        return findmax(node.right)

def delete(node, val):
    if node == None:
        return False

    found, f_node, p_node = query(node, node, val)
    if found == False:
        return False
    elif f_node.left == None:
        if f_node == p_node.left:
            p_node.left = f_node.right
        elif f_node == p_node.right:
            p_node.right = f_node.right
    elif f_node.right == None:
        if f_node == p_node.left:
            p_node.left = f_node.left
        elif f_node == p_node.right:
            p_node.right = f_node.left
    else:
        min_node = findmin(f_node.right)
        f_node.data = min_node.data
        print("f_node:", f_node.data)
        delete(min_node, min_node.data)

    return True

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
    print()

tree = insert(None, 10)
insert(tree, 2)
insert(tree, 31)
insert(tree, 4)
insert(tree, 5)
level_order(tree)
found, node, parent = query(tree, tree, 31)
print("bst find: ", found, "\tparent data: ", parent.data)
print("findmin: ", findmin(tree))
print("findmax: ", findmax(tree))
delete(tree, 2)
level_order(tree)
