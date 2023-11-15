'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def sortList(head):
    z , o, t = 0, 0, 0
    tmp = head

    while tmp != None:
        if tmp.data == 0:
            z += 1
        elif tmp.data == 1:
            o += 1
        else:
            t += 1
        tmp = tmp.next

    tmp = head

    while tmp != None:
        if z != 0:
            tmp.data = 0
            z -= 1
        elif o != 0:
            tmp.data = 1
            o -= 1
        elif t != 0:
            tmp.data = 2
            t -= 1
        tmp = tmp.next
    
    return head
    