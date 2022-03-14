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
    def preOrder(self):
        print (self.val)
        if self.leftchild:
            self.leftchild.preOrder()
        if self.rightchild:
            self.rightchild.preOrder()

    def inOrder(self):
        if self.leftchild:
            self.leftchild.inOrder()
        print (self.val)
        if self.rightchild:
            self.rightchild.inOrder()
    def postOrder(self):
        if self.leftchild:
            self.leftchild.postOrder()
        if self.rightchild:
            self.rightchild.postOrder()
        print (self.val)





    def find(self,data):
        if self.val==data:
            return True
        if data<self.val:
            if self.leftchild:
                return self.leftchild.find(data)
            else:
                return False
        elif data>self.val:
            if self.rightchild:
                return self.rightchild.find(data)
            else:
                return False

def inorderoutside(root):
    if root is None:
       return
    if root.leftchild:
        inorderoutside(root.leftchild)
    print(root.val)
    if root.rightchild:
        inorderoutside(root.rightchild)


def levelOrderTraversalprint(root):
    if root is None:
        return
    queue=deque()
    queue.append(root)
    while(len(queue)>0):
        node=queue.popleft()
        print (node.val)
        if node.leftchild:
            queue.append(node.leftchild)
        if node.rightchild:
            queue.append(node.rightchild)

def levelOrder(root):
    levels=[]
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
            levels[level].append(node.val)
            if node.leftchild:
                queue.append(node.leftchild)
            if node.rightchild:
                queue.append(node.rightchild)
        level=level+1
    return levels

def SearchElement(root,data):
    if root is None:
        return False
    elif root.val==data:
        return True
    elif data<root.val:
        return SearchElement(root.leftchild,data)
    elif data>root.val:
        return SearchElement(root.rightchild,data)

def serialize(root):
    def rserealize(root,string):
        if root is None:
            string+='None,'
        else:
            string+=str(root.val)+','
            string=rserealize(root.leftchild,string)
            string=rserealize(root.rightchild,string)
        return string

    return rserealize(root,'')
def deserialize(data):
    def deserialhelper(data_list):
        if data_list[0]=='None':
            data_list.pop(0)
            return None
        root=Node(data_list[0])
        data_list.pop(0)
        root.leftchild=deserialhelper(data_list)
        root.rightchild=deserialhelper(data_list)
        return root
    data_list=data.split(',')
    print (data_list)
    deserialhelper(data_list)



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
#root.preOrder()
#root.inOrder()
#root.postOrder()
#print (root.find(40))
#levelOrderTraversalprint(root)
#inorderoutside(root)
#print (levelOrder(root))
#print (SearchElement(root,5))
data= serialize(root)
print (data)
print (deserialize(data))



