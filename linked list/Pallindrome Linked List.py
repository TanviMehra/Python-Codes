class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self,data):
        newNode=Node(data)
        if self.head:
            current=self.head
            while(current.next):
                current=current.next
            current.next=newNode
        else:
            self.head=newNode


    def printLList(self):
        current=self.head
        my_list=[]
        while(current):
            my_list.append(current.val)
            current=current.next
        return my_list




obj=LinkedList()
obj.insert(23)
obj.insert(6)
obj.insert(23)
straight=obj.printLList()

if straight==straight[::-1]:
    print (True)
else:
    print (False)
#print (obj.listLength())
#print (obj.get(5))
#obj.delete(15)
#obj.printLList()
#obj.deleteAtIndex(2)
