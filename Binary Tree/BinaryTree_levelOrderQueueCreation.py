from collections import deque
class Node:
    def __init__(self,val):
        self.val=val
        self.leftchild=None
        self.rightchild=None
        self.next=None

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


def nextPointer(root):
    queue=deque()
    queue.append(root)

    while queue:
        size = len(queue)
        for i in range(size):
            node=queue.popleft()
            if i<size-1:
                node.next=queue[0]
            if node.leftchild:
                queue.append(node.leftchild)
            if node.rightchild:
                queue.append(node.rightchild)
    return root

def connect(root):
    if root is None:
        return root
    leftmost=root

    while leftmost.leftchild:
        head=leftmost
        while head:
            head.leftchild.next=head.rightchild
            if head.next:
                
                head.rightchild.next=head.next.leftchild
            head=head.next
        leftmost=leftmost.leftchild
    return root



def levelOrder(root):
    levels=[]
    my_stack=[]
    if root is None:
        return levels
    level=0
    queue=deque()
    queue.append(root)
    while queue:
        levels.append([])
        level_length=len(queue)
        for i in range(level_length):
            node=queue.popleft()
            my_stack.append(node)
            levels[level].append(node.val)
            if node.leftchild:
                queue.append(node.leftchild)
            if node.rightchild:
                queue.append(node.rightchild)
        my_stack.append(None)
        level=level+1
    print (my_stack)
    for i in range(len(my_stack)-1):
        if my_stack[i]!=None:
            my_stack[i].next=my_stack[i+1]
    print (my_stack[2].next)
    return levels


root= Node(10)
root.insert(7)
root.insert(6)
root.insert(12)
root.insert(8)
root.insert(20)
#root.insert(1)
#root.insert(9)
root.insert(11)

#root.preOrder()
#root.inOrder()
#root.postOrder()
#print (root.find(40))
#levelOrderTraversalprint(root)
#inorderoutside(root)
print (levelOrder(root))
#print (nextPointer(root))
print (connect(root))



