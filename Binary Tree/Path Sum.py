
from collections import deque
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def PathSum(root,sum):
    if root is None:
        return False
    if root.left is None and root.right is None:
        return sum==root.val
    return PathSum(root.left,sum-root.val) or PathSum(root.right,sum-root.val)

def PathSumArray(root,sum,path):
    if root is None:
        return False
    if root.left is None and root.right is None:
        if (root.val==sum):
            path.append(root.val)
            return True
        return False
    if (PathSumArray(root.left,sum-root.val,path)):
        path.append(root.val)
        return True
    if (PathSumArray(root.right,sum-root.val,path)):
        path.append(root.val)
        return True
    return False



root= Node(5)
root.left=Node(4)
root.right=Node(8)
root.left.left=Node(11)
root.right.left=Node(13)
root.right.right=Node(4)
root.left.left.left=Node(7)
root.left.left.right=Node(2)
root.right.right.right=Node(1)
#print (PathSum(root,22))
path=[]
PathSumArray(root,22,path)
print (path)






