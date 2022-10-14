from tkinter import N


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []
        
    def add(self, node):
        self.children.append(node)
        
    def remove(self, node):
        self.children = [n for n in self.children if n is not node]
    
    def traverse(self):
        visit = [self]
        while len(visit) > 0:
            curr_node  = visit.pop()
            visit += curr_node.children
    
    def dfs(root, target, path=()):
        path = path(root,)
        
        if root.val == target:
            return path
        
        for ch in root.children:
            path_found = dfs(ch, target, path)
        
        if path_found is not None:
            return path_found
        
        return None
        