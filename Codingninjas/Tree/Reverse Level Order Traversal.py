# Following is the TreeNode class structure:
class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def reverseLevelOrder(root):
    if not root:
        return []
    
    result = []
    stack = []
    queue = [root]

    while queue:
        curr = queue.pop(0)
        stack.append(curr)
        
        if curr.left:
            queue.append(curr.left)
        
        if curr.right:
            queue.append(curr.right)
    
    while stack:
        result.append(stack.pop().val)
    
    return result