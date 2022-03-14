from collections import deque
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

    def insert(self,data):
        if self.val==data:
            return False

        elif self.val>data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left=Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right=Node(data)
                return True
def inOrder(root):

    def inOrderHelper(root,path,paths):
        if not root:
            return
        path.append(root.val)
        if not root.left and not root.right:
            paths.append("->".join(map(str,path)))

        inOrderHelper(root.left,path,paths)
        inOrderHelper(root.right,path,paths)
        path.pop()
        return paths
    return inOrderHelper(root,[],[])

def pathsPrint(root):
    def pathHelper(root,path,paths):
        if root:
            path+=str(root.val)
            if not root.left and not root.right:
                paths.append(path)
            else:
                path+='->'
                pathHelper(root.left,path,paths)
                pathHelper(root.right,path,paths)
        return paths

    return pathHelper(root,'',[])


def pathPrintUsingList(root):
    def printHelper(root,path,paths):
        if not root:
            return
        path.append(root.val)
        if not root.left and not root.right:
            paths.append("->".join(map(str,path)))

        printHelper(root.left,path,paths)
        printHelper(root.right,path,paths)
        path.pop()
        return paths
    return printHelper(root,[],[])

def pathPrintUsingStack(root):
    if root is None:
        return []
    paths=[]
    stack=[(root,str(root.val))]
    while stack:
        node,path=stack.pop()
        if not node.left and not node.right:
            paths.append(path)
        if node.left:
            stack.append((node.left,path+'->'+str(node.left.val)))
        if node.right:
            stack.append((node.right,path+'->'+str(node.right.val)))
    return paths









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
print (PreOrder(root))
'''print (inOrder(root))
print (pathsPrint(root))
print (pathPrintUsingList(root))
print (pathPrintUsingStack(root))'''



