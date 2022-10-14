#create Node

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    
    # Insert new node
def insert(node, data):
    # Return new node if the node empty
    if node is None:
        return Node(data)
    
    #Find the right place and insert the new node
    if data < node.data:
        node.left = insert(node.left, data)
    else:
        node.right = insert(node.right, data)
    return node


def inorderPrint(node):
    if node:
        
        # Traversal left
        inorderPrint(node.left)
        
        # Traversal root
        print(str(node.data) + "->", end=' ')
        
        #Traversal right
        inorderPrint(node.right)
    
def minValue(node):
    curr = node
    
    #find the left most leaf
    while curr.left:
        curr = curr.left
        
    return curr

# deleting node , fist, last and middle node
def deleteNode(node, data):
    #return if the tree is empty
    if node is None:
        return node
    
    #find the node to be deleted
    if data < node.data:
        node.left = deleteNode(node.left, data)
    elif data > node.data:
        node.right = deleteNode(node.right, data)
    else:
        #if the node is only one child or no child
        if node.left is None:
            tmp = node.right
            node = None
            return tmp
        elif node.right is None:
            tmp = node.left
            node = None
            return tmp
        
        #if the node has two children
        #place the inorder successor is position of the node to be deleted
        tmp = minValue(node.right)
        print(tmp.data)
        node.data = tmp.data
        print(node.right.data)
        #delete the inorder successor
        node.right = deleteNode(node.right, tmp.data)
        
    return node


root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root,1)
root = insert(root,6)
root = insert(root,7)
root = insert(root,10)
root = insert(root,14)
root = insert(root,4)
root = insert(root,9)

print("Inorder Traversal: ", end=' ')
inorderPrint(root)
print()

print("Delete Node 8")
root = deleteNode(root, 8)

print("Inorder Traversal: ", end=' ')
inorderPrint(root)
print()
# root = insert(root,10)
# print("Inorder Traversal: ", end=' ')
# inorderPrint(root)
# print()