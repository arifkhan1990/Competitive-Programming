class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        
#calculate the depth of the tree
def calculateDepth(node):
    depth = 0
    
    while node:
        depth, node = depth + 1, node.left
    return depth

#check if the tree is perfect binary tree
def is_perfect_binary(node, depth, level=0):
    # print(depth, level, end=' ')
    #if the tree is empty
    if node is None:
        return True
    
    if node.left is None and node.right is None:
        if depth == level + 1:
            return True
        else:
            return False
    
    return (is_perfect_binary(node.left, depth, level+1) and is_perfect_binary(node.right, depth, level+1))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.left.left= Node(9)

if is_perfect_binary(root, calculateDepth(root)):
    print("Yes This Tree is perfect binary tree.")
else:
    print("No! This Tree is Not perfect binary tree.")

    