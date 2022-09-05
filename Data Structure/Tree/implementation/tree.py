class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
    
    def inorderTraversal(self, root):
        ans = []
        if root:
            ans = ans + self.inorderTraversal(root.left)
            ans.append(root.data)
            ans = ans + self.inorderTraversal(root.right)
        return ans
    
    def preorderTraversal(self, root):
        ans = []
        if root:
            ans.append(root.data)
            ans = ans + self.preorderTraversal(root.left)
            ans = ans + self.preorderTraversal(root.right)
        return ans
    
    def postorderTraversal(self, root):
        ans = []
        if root:
            ans = ans + self.postorderTraversal(root.left)
            ans = ans + self.postorderTraversal(root.right)
            ans.append(root.data)
        return ans
    
    def findValue(self, data):
        if data < self.data:
            if self.left is None:
                return "Not Found!"
            else:
                return self.left.findValue(data)
        elif data > self.data:
            if self.right is None:
                return "Not Found!"
            else:
                return self.right.findValue(data)
        else:
            return "Found"
                    
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(15)
root.insert(9)

# root.printTree()

print(root.inorderTraversal(root))
print(root.preorderTraversal(root))
print(root.postorderTraversal(root))

print(root.findValue(0))
print(root.findValue(15))
            