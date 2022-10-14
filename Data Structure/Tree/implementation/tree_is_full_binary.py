class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def insert(self, node, data):
    if node is None:
        return node
    
    if data < node.data:
        node.left = insert(node.left, data)
    else:
        node.right = insert(node.right, data)
    
    return node

def isFullBinary(node):
    print(node.data,end=' ')
    if node is None:
        return True
        
    if node.left is None and node.right is None:
        return True
    
    if node.left is not None and node.right is not None:
        return (isFullBinary(node.left) and isFullBinary(node.right))
    
    return False


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)
root.right.left = Node(8)
root.right.right = Node(9)
root.left.left.left= Node(11)
root.left.left.right = Node(12)
if isFullBinary(root):
    print("Yes")
else:
    print("No")
            