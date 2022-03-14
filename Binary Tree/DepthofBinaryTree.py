from collections import deque
class Node:
    def __init__(self,val):
        self.val=val
        self.leftchild=None
        self.rightchild=None

    def insert(self,data):
        if self.val==data:
            return False

        elif self.val>data:
            if self.leftchild:
                return self.leftchild.insert(data)
            else:
                self.leftchild=Node(data)
                return True
        else:
            if self.rightchild:
                return self.rightchild.insert(data)
            else:
                self.rightchild=Node(data)
                return True
def maxDepth(root):
    if root is None:
        return 0
    leftd=maxDepth(root.leftchild)

    rightd=maxDepth(root.rightchild)
    return max(leftd,rightd)+1



root= Node(10)
root.insert(7)
root.insert(6)
root.insert(11)
root.insert(8)
root.insert(20)
root.insert(1)
root.insert(9)
root.insert(14)
root.insert(22)
print (maxDepth(root))



